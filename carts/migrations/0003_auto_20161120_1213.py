# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_auto_20161120_1156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='Quantity',
            new_name='quantity',
        ),
    ]
