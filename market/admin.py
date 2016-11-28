from django.contrib import admin
from .models import Profile, Categories, SubCategories, States, Lga, Stores, Items, ItemImages, Cart, ShippingAddress, Order

# Register your models here.
admin.site.register(Profile)
admin.site.register(Categories)
admin.site.register(SubCategories)
admin.site.register(States)
admin.site.register(Lga)
admin.site.register(Stores)
admin.site.register(Items)
admin.site.register(ItemImages)
admin.site.register(Cart)
admin.site.register(ShippingAddress)
admin.site.register(Order)