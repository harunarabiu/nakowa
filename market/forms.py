from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

)
from .models import Profile, Items, Stores, Cart
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone']


class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['item_title', 'item_category', 'item_subcategory', 'item_state', 'item_location',
                  'item_price', 'item_image', 'item_price', 'item_description']


class LoginForm(forms.Form):
    User = get_user_model()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")
            if not user.is_active:
                raise forms.ValidationError("This user is not active")

        return super(LoginForm, self).clean(*args, **kwargs)


class StoreForm(forms.ModelForm):
    class Meta:
        model = Stores
        fields = ['store_name', 'store_category', 'store_phone', 'store_state', 'store_lga',
                  'store_address', 'store_description']


class AddtoCart(forms.ModelForm):
    cart_user = forms.IntegerField(widget=forms.HiddenInput())
    cart_itemStore = forms.IntegerField(widget=forms.HiddenInput())
    cart_item = forms.IntegerField(widget=forms.HiddenInput())
    cart_itemQty = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Cart
        fields = ['cart_user', 'cart_itemStore', 'cart_item', 'cart_itemQty']

