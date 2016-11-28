# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carts', '0004_auto_20161120_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_id', models.CharField(default=b'ABC', unique=True, max_length=255)),
                ('tax_total', models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)),
                ('final_total', models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)),
                ('sub_total', models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)),
                ('status', models.CharField(default=b'Started', max_length=255, choices=[(b'Started', b'Started'), (b'Abandoned', b'Abandoned'), (b'Finished', b'Finished')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cart', models.ForeignKey(to='carts.MyCart')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
