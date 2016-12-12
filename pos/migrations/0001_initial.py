# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 18:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=16)),
                ('long_name', models.CharField(max_length=128)),
                ('manager_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_visible', models.BooleanField()),
                ('name', models.CharField(max_length=128)),
                ('business', models.CharField(max_length=128)),
                ('rut', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=128)),
                ('contact_name', models.CharField(max_length=128)),
                ('contact_area', models.CharField(max_length=128)),
                ('contact_email', models.CharField(max_length=128)),
                ('previous_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.Provider')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folio_number', models.CharField(max_length=128)),
                ('payment_conditions', models.CharField(max_length=128)),
                ('payment_method', models.CharField(max_length=128)),
                ('contract_number', models.CharField(max_length=128)),
                ('quotation_order', models.CharField(max_length=128)),
                ('total_price', models.IntegerField()),
                ('currency', models.CharField(max_length=128)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.Provider')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=128)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('currency', models.CharField(max_length=8)),
                ('purchase_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.PurchaseOrder')),
            ],
        ),
        migrations.CreateModel(
            name='YapoUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.Area')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='yapo_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.YapoUser'),
        ),
    ]
