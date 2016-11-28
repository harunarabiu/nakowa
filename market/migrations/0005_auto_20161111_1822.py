# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_items_item_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='item_store',
            field=models.ForeignKey(to='market.Stores'),
        ),
    ]
