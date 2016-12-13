# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-13 13:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='long_name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='area',
            name='manager_name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='area',
            name='short_name',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='address',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='business',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='contact_area',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='contact_email',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='contact_name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='phone',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='previous_provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pos.Provider'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='rut',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='contract_number',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='currency',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='folio_number',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='payment_conditions',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='payment_method',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pos.Provider'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='quotation_order',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='total_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='yapo_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pos.YapoUser'),
        ),
        migrations.AlterField(
            model_name='purchaseorderdetail',
            name='description',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorderdetail',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='purchaseorderdetail',
            name='purchase_order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pos.PurchaseOrder'),
        ),
        migrations.AlterField(
            model_name='purchaseorderdetail',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='yapouser',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pos.Area'),
        ),
        migrations.AlterField(
            model_name='yapouser',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]