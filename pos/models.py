from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Area(models.Model):
    short_name = models.CharField(max_length=16, null=True, blank=True)
    long_name = models.CharField(max_length=128, null=True, blank=True)
    manager_name = models.CharField(max_length=128, null=True, blank=True)
    manager_position = models.CharField(max_length=128, null=True, blank=True)

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
    area = models.ForeignKey(Area, null=True, blank=True)
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

    def set_folio_number(self):
        self.folio_number = datetime.now().strftime('%Y%m%d%H%M%S')
        self.folio_number = self.area.short_name + self.folio_number

    def set_total_price(self):
        self.total_price = 0
        for detail in self.purchaseorderdetail_set.all():
            self.total_price += detail.price

    def set_order_data(self):
        self.set_folio_number()
        self.set_total_price()
        self.save()

    def create_from_request(request):
        # get data
        detail_name = request.POST.getlist('detail_name[]')
        quantity = request.POST.getlist('quantity[]')
        price = request.POST.getlist('price[]')
        currency = request.POST.get('currency')
        provider = request.POST.get('provider')
        quotation_order = request.POST.get('quotation_order')
        payment_method = request.POST.get('payment_method')
        payment_condition = request.POST.get('payment_condition')
        contract_number = request.POST.get('contract_number')
        user_area = request.POST.get('user_area')
        # create purchase order
        new_po = PurchaseOrder()
        new_po.is_visible = False
        new_po.quotation_order = quotation_order
        new_po.contract_number = contract_number
        # Try to get currency, provider, payment data and area, form ids given in request
        try:
            new_po.currency = Currency.objects.get(pk=currency)
            new_po.provider = Provider.objects.get(pk=provider)
            new_po.payment_method = PaymentMethod.objects.get(pk=payment_method)
            new_po.payment_conditions = PaymentCondition.objects.get(pk=payment_condition)
            new_po.area = Area.objects.get(pk=user_area)
            # Save this po. If invalid data found, it will raise a ValueError
            new_po.save()
        except (ValueError, Currency.DoesNotExist, Provider.DoesNotExist,
            PaymentMethod.DoesNotExist, PaymentConditions.DoesNotExist):
            return None
        # crete details
        for new_description, new_quantity, new_price in zip(detail_name, quantity, price):
            # Ignore empty details
            if (new_description == '') or (new_quantity == '') or (new_price == ''):
                continue
            new_detail = PurchaseOrderDetail()
            new_detail.description = new_description
            new_detail.quantity = new_quantity
            new_detail.price = new_price
            try:
                # If a detail have invalid data, ti will raise a ValueError
                new_detail.save()
            except ValueError:
                new_po.delete()
                return None
            new_po.purchaseorderdetail_set.add(new_detail)
        new_po.set_order_data()
        # purchase order was created, we can redirect
        return new_po

class PurchaseOrderDetail(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, null=True, blank=True)
    description = models.CharField(max_length=128, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    currency = models.ForeignKey(Currency, null=True, blank=True)

    def __str__(self):
        return self.description
