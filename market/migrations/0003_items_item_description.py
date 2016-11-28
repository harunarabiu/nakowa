# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_auto_20161111_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='item_description',
            field=models.TextField(default=1, max_length=2000),
            preserve_default=False,
        ),
    ]
