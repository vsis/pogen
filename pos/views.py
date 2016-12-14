from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

from .models import Area, Provider, PurchaseOrder

class ListView(generic.ListView):
    template_name = 'pos/pos_list.html'
    context_object_name = 'pos_list'
 
    def get_queryset(self):
        return PurchaseOrder.objects.all()

class DetailView(generic.DetailView):
    model = PurchaseOrder
    template_name = 'pos/detail.html'

def new_po(request):
    areas = Area.objects.all()
    providers = Provider.objects.filter(is_visible=True)
    return render(request, 'pos/new_po.html', {'areas': areas, 'providers': providers})

def post_po(request):
    pass
