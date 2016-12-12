from django.shortcuts import render
from django.views import generic

from .models import PurchaseOrder

class DetailView(generic.DetailView):
    model = PurchaseOrder
    template_name = 'pos/detail.html'

def new_po(request):
    pass

def post_po(request):
    pass
