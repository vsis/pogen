from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Area(models.Model):
    short_name = models.CharField(max_length=16, null=True, blank=True)
    long_name = models.CharField(max_length=128, null=True, blank=True)
    manager_name = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.long_name


class YapoUser(models.Model):
    area = models.ForeignKey(Area, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Provider(models.Model):
    previous_provider = models.ForeignKey('self', null=True, blank=True)
    is_visible = models.BooleanField()
    name = models.CharField(max_length=128, null=True, blank=True)
    business = models.CharField(max_length=128, null=True, blank=True)
    rut = models.CharField(max_length=128, null=True, blank=True)
    address = models.CharField(max_length=128, null=True, blank=True)
    phone = models.CharField(max_length=128, null=True, blank=True)
    contact_name = models.CharField(max_length=128, null=True, blank=True)
    contact_area = models.CharField(max_length=128, null=True, blank=True)
    contact_email = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class PaymentMethod(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class PaymentCondition(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class PurchaseOrder(models.Model):
    yapo_user = models.ForeignKey(YapoUser, null=True, blank=True)
    provider = models.ForeignKey(Provider, null=True, blank=True)
    folio_number = models.CharField(max_length=128, null=True)
    payment_conditions = models.ForeignKey(PaymentCondition, null=True, blank=True)
    payment_method = models.ForeignKey(PaymentMethod, null=True, blank=True)
    contract_number = models.CharField(max_length=128, null=True, blank=True)
    quotation_order = models.CharField(max_length=128, null=True, blank=True)
    total_price = models.IntegerField(null=True, blank=True)
    currency = models.ForeignKey(Currency, null=True, blank=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.folio_number

    def set_folio_number(self, short_name_area=None):
        self.folio_number = datetime.now().strftime('%Y%m%d%H%M%S')
        if short_name_area != None:
            self.folio_number = short_name_area + self.folio_number

    def set_total_price(self):
        self.total_price = 0
        for detail in self.purchaseorderdetail_set.all():
            self.total_price += detail.price

    def set_order_data(self, short_area_name=None):
        self.set_folio_number(short_area_name)
        self.set_total_price()
        self.save()

class PurchaseOrderDetail(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, null=True, blank=True)
    description = models.CharField(max_length=128, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    currency = models.ForeignKey(Currency, null=True, blank=True)

    def __str__(self):
        return self.description
