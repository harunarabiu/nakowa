from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from market.models import Items
from .models import MyCart, CartItem
# Create your views here.


def view(request):
    try:
        the_id = request.session['cart_id']
        cart = MyCart.objects.get(id=the_id)
    except:
        the_id = None
    if the_id:
        new_total = 0.00
        for item in cart.cartitem_set.all():
            line_total = float(item.product.item_price) * item.quantity
            new_total += line_total

        request.session["items_total"] = cart.cartitem_set.count()
        cart.total = new_total
        cart.save()
        context = {"cart": cart}
    else:
        message = "Your Cart is Empty"
        context = {"empty": True, "message": message}

    template = "cart/view.html"

    return render(request, template, context)


def remove_from_cart(request, id):
    try:
        the_id = request.session['cart_id']
        cart = MyCart.objects.get(id=the_id)
    except:
        return HttpResponseRedirect(reverse("cart"))

    cartitem = CartItem.objects.get(id=id)
    #cartitem.delete()
    cartitem.cart = None
    cartitem.save()
    return HttpResponseRedirect(reverse("cart"))


def update_cart(request, pk=None):

    request.session.set_expiry(86400)
    try:
        qty = request.GET.get('qty')
        update_qty = True
    except:
        qty = None
        update_qty = False


    try:
        the_id = request.session['cart_id']
    except:
        new_cart = MyCart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = MyCart.objects.get(id=the_id)

    try:
        product = Items.objects.get(pk=pk)
    except Items.DoesNotExist:
        pass
    except:
        pass

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if created:
        print("created")
    if update_qty and qty:
        if int(qty) == 0:
            cart_item.delete()
        else:
            cart_item.quantity = qty
            cart_item.save()
    else:
        pass

    # if not cart_item in cart.items.all():
    #     cart.items.add(cart_item)
    # else:
    #     cart.items.remove(cart_item)


    return HttpResponseRedirect(reverse("cart"))