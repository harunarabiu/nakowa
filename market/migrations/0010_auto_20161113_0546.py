# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0009_auto_20161113_0541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemimages',
            name='image_status',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='items',
            name='item_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.ForeignKey(default=0, to='market.States'),
        ),
    ]
