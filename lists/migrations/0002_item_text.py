# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-01 04:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='text',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]