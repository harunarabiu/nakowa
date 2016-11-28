from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^market/', include('market.urls')),
    url(r'^s/$', 'market.views.search_view', name="search"),
    url(r'^cart/$', 'carts.views.view', name="cart"),
    url(r'^cart/(?P<pk>\d+)/$', 'carts.views.update_cart', name="update_cart"),
    url(r'^cart/(?P<id>\d+)/remove/$', 'carts.views.remove_from_cart', name="remove_from_cart"),
    url(r'^category/(?P<pk>\d+)/$', 'market.views.category_view', name="category"),
    url(r'^checkout/$', 'orders.views.checkout', name="checkout"),
    url(r'^orders/$', 'orders.views.orders', name="orders"),
]
