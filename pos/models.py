from django.db import models
from django.contrib.auth.models import User


class Area(models.Model):
    short_name = models.CharField(max_length=16)
    long_name = models.CharField(max_length=128)
    manager_name = models.CharField(max_length=128)

    def __str__(self):
        return self.long_name


class YapoUser(models.Model):
    area = models.ForeignKey(Area)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Provider(models.Model):
    previous_provider = models.ForeignKey('self')
    is_visible = models.BooleanField()
    name = models.CharField(max_length=128)
    business = models.CharField(max_length=128)
    rut = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    contact_name = models.CharField(max_length=128)
    contact_area = models.CharField(max_length=128)
    contact_email = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class PurchaseOrder(models.Model):
    yapo_user = models.ForeignKey(YapoUser)
    provider = models.ForeignKey(Provider)
    folio_number = models.CharField(max_length=128)
    payment_conditions = models.CharField(max_length=128)
    payment_method = models.CharField(max_length=128)
    contract_number = models.CharField(max_length=128)
    quotation_order = models.CharField(max_length=128)
    total_price = models.IntegerField()
    currency = models.CharField(max_length=128)

    def __str__(self):
        return self.folio_number


class PurchaseOrderDetail(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder)
    description = models.CharField(max_length=128)
    quantity = models.IntegerField()
    price = models.IntegerField()
    currency = models.CharField(max_length=8)

    def __str__(self):
        return self.description
