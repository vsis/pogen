# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 01:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0004_auto_20161215_0143'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PaymentConditions',
            new_name='PaymentCondition',
        ),
    ]
