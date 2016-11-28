# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_auto_20161111_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='item_store',
            field=models.ForeignKey(to='market.Stores', null=True),
        ),
    ]
