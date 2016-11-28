import time
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import render, HttpResponseRedirect
from carts.models import MyCart
from .models import MyOrder


def orders(request):
    try:
        user = request.user
        orders = user.myorder_set.all
        orders_total = user.myorder_set.count()
    except:
        user = None

    if orders_total < 1:
        context = {"empty": True}
    else:
        context = {"orders": orders}

    template = "orders/orders.html"
    return render(request, template, context)

#login Required
def checkout(request):
    try:
        the_id = request.session['cart_id']
        cart = MyCart.objects.get(id=the_id)
    except:
        the_id = None
        return HttpResponseRedirect(reverse("cart"))

    new_order, created = MyOrder.objects.get_or_create(cart=cart)
    if created:
        # assign a user to the order
        new_order.order_id = str(time.time())
        new_order.user = request.user
        new_order.save()
        #assign address run Credit card
    if new_order.status == "Finished":
       # cart.delete()
        del request.session['cart_id']
        del request.session["items_total"]
        return HttpResponseRedirect(reverse("cart"))

    context = {}
    template = "orders/checkout.html"

    return render(request, template, context)


