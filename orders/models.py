from django.db import models
from django.contrib.auth.models import User
from carts.models import MyCart
# Create your models here.

STATUS_CHOICES = (

    ("Started", "Started"),
    ("Abandoned", "Abandoned"),
    ("Finished", "Finished"),
)


class MyOrder(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    order_id = models.CharField(max_length=255, default='ABC', unique=True)
    cart = models.ForeignKey(MyCart)
    tax_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    final_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    sub_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default="Started")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self. order_id

