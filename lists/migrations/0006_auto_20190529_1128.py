# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-29 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_auto_20190522_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(blank=True, default=''),
        ),
    ]
