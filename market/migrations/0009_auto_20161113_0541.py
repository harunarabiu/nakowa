# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0008_auto_20161112_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.ForeignKey(to='market.States', blank=True),
        ),
    ]
