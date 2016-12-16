from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import generic
from django.urls import reverse

from .models import PaymentMethod, PaymentCondition, PurchaseOrderDetail, Currency, Area, Provider, PurchaseOrder

class ListView(generic.ListView):
    template_name = 'pos/pos_list.html'
    context_object_name = 'pos_list'
 
    def get_queryset(self):
        return PurchaseOrder.objects.filter(is_visible=True)

class DetailView(generic.DetailView):
    model = PurchaseOrder
    template_name = 'pos/detail.html'

def new_po(request):
    areas = Area.objects.all()
    providers = Provider.objects.filter(is_visible=True)
    currencies = Currency.objects.all()
    payment_methods = PaymentMethod.objects.all()
    payment_conditions = PaymentCondition.objects.all()
    return render(request, 'pos/new_po.html', 
            {
                'areas': areas,
                'providers': providers,
                'currencies': currencies,
                'payment_methods': payment_methods,
                'payment_conditions': payment_conditions,
            }
    )

def preview_po(request):
    # user wants to store purchase order
    if request.method == 'POST': 
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
        new_po.provider = Provider.objects.get(pk=provider)
        new_po.currency = Currency.objects.get(pk=currency)
        new_po.quotation_order = quotation_order
        new_po.contract_number = contract_number
        new_po.payment_method = PaymentMethod.objects.get(pk=payment_method)
        new_po.payment_conditions = PaymentCondition.objects.get(pk=payment_condition)
        new_po.area = Area.objects.get(pk=user_area)
        new_po.save()
        # crete details
        for new_description, new_quantity, new_price in zip(detail_name, quantity, price):
            new_detail = PurchaseOrderDetail()
            new_detail.description = new_description
            new_detail.quantity = new_quantity
            new_detail.price = new_price
            new_detail.save()
            new_po.purchaseorderdetail_set.add(new_detail)
        new_po.set_order_data()
        # purchase order was created, we can redirect
        return HttpResponseRedirect(reverse('pos:detail_po', args=[new_po.pk,]))
    else:
        raise Http404

def post_po(request):
    order_id = request.POST.get('order_id')
    try:
        order = PurchaseOrder.objects.get(pk=order_id)
        order.is_visible = True
        order.save()
        return HttpResponseRedirect(reverse('pos:detail_po', args=[order.pk,]))
    except PurchaseOrder.DoesNotExist:
        raise Http404
