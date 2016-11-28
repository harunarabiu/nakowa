# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_items_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='item_store',
            field=models.ForeignKey(default=0, to='market.Stores'),
        ),
    ]
