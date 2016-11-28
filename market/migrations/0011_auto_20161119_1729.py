# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import market.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('market', '0010_auto_20161113_0546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cart_itemStore', models.IntegerField(verbose_name=market.models.Stores)),
                ('cart_itemQty', models.IntegerField()),
                ('cart_item', models.ForeignKey(to='market.Items')),
                ('cart_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_itemQty', models.IntegerField()),
                ('order_date', models.IntegerField()),
                ('order_status', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sa_contactName', models.CharField(max_length=255)),
                ('sa_phone', models.CharField(max_length=25)),
                ('sa_streetAddress', models.CharField(max_length=255)),
                ('sa_status', models.IntegerField(default=0)),
                ('sa_lga', models.ForeignKey(to='market.Lga')),
                ('sa_state', models.ForeignKey(to='market.States')),
                ('sa_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='order_ShippingAddress',
            field=models.ForeignKey(to='market.ShippingAddress'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_item',
            field=models.ForeignKey(to='market.ItemImages'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_itemStore',
            field=models.ForeignKey(to='market.Stores'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
