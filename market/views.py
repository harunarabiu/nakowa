from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.views import generic
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from .forms import UserForm, ProfileForm, ItemForm, LoginForm, StoreForm, AddtoCart
from django.contrib import messages
from django.db import transaction
from .models import Items, Stores, Profile
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

#def index(request):
    #return HttpResponse("<h2>Welcome to the market place</h2>")

#def index(request):
    #template = loader.get_template('market/index.html')
    #return HttpResponse(template.render(request))

#def index(request):
    #return render(request, 'market/index.html')


def index_home(request):
    template_name = "market/index.html"
    items = Items.objects.all()
    return render(request, template_name, {'items': items})


def category_view(request, pk=None):
    template_name = "market/category.html"
    items = Items.objects.filter(item_category=pk)
    return render(request, template_name, {'items': items})


def search_view(request):
    template_name = "market/search.html"
    try:
        q = request.GET.get('q')
    except:
        q = None

    if q:
        items = Items.objects.filter(item_title__icontains = q)
        return render(request, template_name, {'items': items})
    else:
        items = Items.objects.filter(item_title__icontains=q)
        return render(request, template_name, {'items': items})


class IndexView(generic.TemplateView):
    template_name = "market/index.html"


class LoginView(generic.TemplateView):
    template_name = "market/login.html"


class RegisterView(generic.TemplateView):
    template_name = "market/register.html"


class ProfileView(generic.ListView):
    template_name = "market/profile.html"


def user_items(request):
    template_name = "market/profile.html"
    #if request.user.is_authenticated:
    items = Items.objects.filter(item_user=request.user.id)
    return render(request, template_name, {'items': items})


def profile_view(request, pk=None):
    template_name = "market/oprofile.html"

    stores = Stores.objects.filter(store_user=pk)
    profile = get_object_or_404(Profile, user=pk)
    profile_items = Items.objects.filter(item_user=pk)

    return render(request, template_name, {'profile': profile, 'stores': stores, 'profile_items': profile_items})


def store_view(request, pk=None):
    template_name = "market/store.html"
    #if request.user.is_authenticated:
    #store = Stores.objects.filter(store_user=id)
    store = get_object_or_404(Stores, pk=pk)
    store_items = Items.objects.filter(item_store=pk)
    latest_items = Items.objects.filter(item_store=pk).order_by('item_createDate')[:4]

    return render(request, template_name, {'store': store, 'store_items': store_items, 'latest_items': latest_items})


#@login_required(login_url='/login/')
class PostItem(View):
    template_name = "market/items_form.html"

    def get(self, request):
        form = ItemForm(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.item_user = request.user
            form.save()
            messages.success(request, "Item Successfully Added")
            return HttpResponseRedirect(item.get_absolute_url())
        return render(request, self.template_name, {'form': form})


def item_details(request, pk=None):
    template_name = "market/item_details.html"
    item = get_object_or_404(Items, pk=pk)
    form = AddtoCart(request.POST)

    if form.is_valid():
        cart = form.save(commit=False)
        cart.cart_user = request.user
        cart.cart_itemStore = item.item_store
        cart.cart_item = item
        cart.cart_itemQty = 1
        form.save()

    return render(request, template_name, {'item': item, 'form': form})


class ItemDetail(View):
    model = Items
    template_name = "market/item_details.html"


class ItemUpdate(UpdateView):
    model = Items
    fields = ['item_user', 'item_title', 'item_category', 'item_subcategory', 'item_state', 'item_location',
              'item_price', 'item_image', 'item_price', 'item_description']


class ItemDelete(DeleteView):
    model = Items
    success_url = reverse_lazy("index")


class UserFormView(View):
    form_class = UserForm
    template_name = 'market/register.html'

    def get(self, request):
        user_form = UserForm(None)
        profile_form = ProfileForm(None)

        return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})

    @transaction.atomic
    def post(self, request):
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            #profile = profile_form.save(commit=False)

            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user.refresh_from_db()
            profile_form = ProfileForm(request.POST, instance=user.profile)
            profile_form.full_clean()
            profile_form.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('index')

        return render(request, self.template_name, {'user_form': user_form, 'profile_form': profile_form})


class StoreFormView(View):
    template_name = 'market/store_form.html'

    def get(self, request):
        form = StoreForm(None)

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = StoreForm(request.POST)
        if form.is_valid():
            store = form.save(commit=False)
            store.store_user = request.user
            form.full_clean()
            form.save()
            return redirect(store.get_absolute_url())
        return render(request, self.template_name, {'form': form})


def store_form(request):
    template_name = 'market/store_form.html'

    form = StoreForm(request.POST or None)
    if form.is_valid():
        store = form.save(commit=False)
        store.store_user = request.user
        form.full_clean()
        form.save()
        return redirect(store.get_absolute_url())
    return render(request, template_name, {'form': form})


def login_view(request):
    template_name = 'market/login.html'

    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('index')
    return render(request, template_name, {'form': form})


def logout_view(request):
    template_name = 'market/index.html'
    logout(request)
    return render(request, template_name, {})




