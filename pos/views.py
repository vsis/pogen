from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import generic
from django.urls import reverse

from .models import PaymentMethod, PaymentCondition, PurchaseOrderDetail, Currency, Area, Provider, PurchaseOrder

class ListView(generic.ListView):
    template_name = 'pos/pos_list.html'
    context_object_name = 'pos_list'
 
    def get_queryset(self):
        return PurchaseOrder.objects.filter(is_visible=True).order_by('-pk')

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
        new_po = PurchaseOrder.create_from_request(request)
        if new_po != None:
            return HttpResponseRedirect(reverse('pos:detail_po', args=[new_po.pk,]))
        else:
            return HttpResponseRedirect(reverse('pos:new_po'))
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
def search_po(request):
    areas = Area.objects.all()
    providers = Provider.objects.filter(is_visible=True)
    return render(request, 'pos/search_po.html',
            {
                'areas': areas,
                'providers': providers,
            }
    )

def filter_po(request, provider=0, area=0):
    pos_list = PurchaseOrder.objects.filter(is_visible=True).order_by('-pk')
    if provider != '0':
        pos_list = pos_list.filter(provider__pk=provider)
    if area != '0':
        pos_list = pos_list.filter(area__pk=area)
    return render(request, 'pos/pos_list.html', {'pos_list': pos_list})

