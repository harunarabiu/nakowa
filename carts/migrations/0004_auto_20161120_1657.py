# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_auto_20161120_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mycart',
            name='items',
        ),
        migrations.RemoveField(
            model_name='mycart',
            name='products',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(blank=True, to='carts.MyCart', null=True),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='line_total',
            field=models.DecimalField(default=10.99, max_digits=1000, decimal_places=2),
        ),
    ]
