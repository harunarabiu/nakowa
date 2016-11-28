from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.db import models


class Categories(models.Model):
    category_name = models.CharField(max_length=255)
    category_description = models.TextField(max_length=2000, blank=True)
    category_status = models.IntegerField(default=0)

    def __str__(self):
        return self.category_name


class SubCategories(models.Model):
    subCategory_category = models.ForeignKey(Categories);
    SubCategory_name = models.CharField(max_length=255)
    SubCategory_description = models.TextField(max_length=2000, blank=True)
    SubCategory_status = models.IntegerField(default=0)

    def __str__(self):
        return self.SubCategory_name


class States(models.Model):
    state_name = models.CharField(max_length=255)

    def __str__(self):
        return self.state_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255, blank=True)
    state = models.ForeignKey(States, default=0)
    city = models.CharField(max_length=255, blank=True)
    address = models.TextField(max_length=2000, blank=True)

    def get_absolute_url(self):
        return reverse('OProfile', kwargs={'pk': self.pk})

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    post_save.connect(create_user_profile, sender=User)

    def __str__(self):
        return self.user.username


class Lga(models.Model):
    lga_name = models.CharField(max_length=255)
    lga_state = models.ForeignKey(States)

    def __str__(self):
        return self.lga_name


class Stores(models.Model):
    store_user = models.ForeignKey(User)
    store_name = models.CharField(max_length=255)
    store_address = models.TextField(max_length=2000)
    store_phone = models.CharField(max_length=255)
    store_description = models.TextField(max_length=2000, blank=True)
    store_state = models.ForeignKey(States)
    store_lga = models.ForeignKey(Lga)
    store_category = models.ForeignKey(Categories)
    store_status = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('Store', kwargs={'pk': self.pk})

    def __str__(self):
        return self.store_name


class Items(models.Model):
    item_user = models.ForeignKey(User)
    item_title = models.CharField(max_length=255)
    item_description = models.TextField(max_length=2000)
    item_category = models.ForeignKey(Categories)
    item_subcategory = models.ForeignKey(SubCategories)
    item_store = models.ForeignKey(Stores, null=True, blank=True)
    item_state = models.ForeignKey(States)
    item_location = models.CharField(max_length=255)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=255)
    item_status = models.IntegerField(default=0)
    item_createDate = models.DateField(auto_now_add=True)
    item_modifiedDate = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse('ItemDetail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.item_title


class ItemImages(models.Model):
    image_item = models.ForeignKey(Items)
    image_name = models.CharField(max_length=255)
    image_status = models.IntegerField()


class Cart(models.Model):
    cart_user = models.ForeignKey(User)
    cart_itemStore = models.ForeignKey(Stores)
    cart_item = models.ForeignKey(Items)
    cart_itemQty = models.IntegerField()


class ShippingAddress(models.Model):
    sa_user = models.ForeignKey(User)
    sa_state = models.ForeignKey(States)
    sa_lga = models.ForeignKey(Lga)
    sa_contactName = models.CharField(max_length=255)
    sa_phone = models.CharField(max_length=25)
    sa_streetAddress = models.CharField(max_length=255)
    sa_status = models.IntegerField(default=0)


class Order(models.Model):
    order_item = models.ForeignKey(ItemImages)
    order_itemStore = models.ForeignKey(Stores)
    order_itemQty = models.IntegerField()
    order_date = models.IntegerField()
    order_user = models.ForeignKey(User)
    order_ShippingAddress = models.ForeignKey(ShippingAddress)
    order_status = models.IntegerField(default=0)

