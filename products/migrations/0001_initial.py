# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('slug', models.SlugField(blank=True)),
                ('description', models.TextField(default=b'')),
                ('price', models.DecimalField(default=9.99, null=True, max_digits=6, decimal_places=2)),
                ('sale_price', models.DecimalField(default=6.99, null=True, max_digits=6, decimal_places=2, blank=True)),
            ],
        ),
    ]
