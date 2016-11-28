# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=255)),
                ('category_description', models.TextField(max_length=2000, blank=True)),
                ('category_status', models.BinaryField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ItemImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_name', models.CharField(max_length=255)),
                ('image_status', models.BinaryField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_title', models.TextField()),
                ('item_location', models.CharField(max_length=255)),
                ('item_price', models.BinaryField(max_length=25)),
                ('item_image', models.CharField(max_length=255)),
                ('item_status', models.IntegerField(default=0)),
                ('item_createDate', models.DateField(auto_now_add=True)),
                ('item_modifiedDate', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lga_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=255, blank=True)),
                ('city', models.CharField(max_length=255, blank=True)),
                ('address', models.TextField(max_length=2000, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Stores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('store_name', models.CharField(max_length=255)),
                ('store_address', models.TextField(max_length=2000)),
                ('store_phone', models.CharField(max_length=255)),
                ('store_description', models.TextField(max_length=2000, blank=True)),
                ('store_status', models.IntegerField(default=0)),
                ('store_category', models.ForeignKey(to='market.Categories')),
                ('store_lga', models.ForeignKey(to='market.Lga')),
                ('store_state', models.ForeignKey(to='market.States')),
                ('store_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('SubCategory_name', models.CharField(max_length=255)),
                ('SubCategory_description', models.TextField(max_length=2000, blank=True)),
                ('SubCategory_status', models.BinaryField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.ForeignKey(to='market.States', blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lga',
            name='lga_state',
            field=models.ForeignKey(to='market.States'),
        ),
        migrations.AddField(
            model_name='items',
            name='item_state',
            field=models.ForeignKey(to='market.States'),
        ),
        migrations.AddField(
            model_name='items',
            name='item_subcategory',
            field=models.ForeignKey(to='market.SubCategories'),
        ),
        migrations.AddField(
            model_name='items',
            name='item_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='itemimages',
            name='image_item',
            field=models.ForeignKey(to='market.Items'),
        ),
    ]
