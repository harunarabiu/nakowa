# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='item_category',
            field=models.ForeignKey(default=1, to='market.Categories'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategories',
            name='subCategory_category',
            field=models.ForeignKey(default=1, to='market.Categories'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categories',
            name='category_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='itemimages',
            name='image_status',
            field=models.IntegerField(max_length=25),
        ),
        migrations.AlterField(
            model_name='items',
            name='item_price',
            field=models.IntegerField(max_length=25),
        ),
        migrations.AlterField(
            model_name='items',
            name='item_title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='subcategories',
            name='SubCategory_status',
            field=models.IntegerField(default=0),
        ),
    ]
