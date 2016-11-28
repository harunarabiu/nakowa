# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0007_auto_20161112_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='item_store',
            field=models.ForeignKey(blank=True, to='market.Stores', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.ForeignKey(to='market.States'),
        ),
    ]
