# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0009_auto_20161220_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]