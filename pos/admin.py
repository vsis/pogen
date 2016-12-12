from django.contrib import admin
from .models import Area, YapoUser, Provider, PurchaseOrder

admin.site.register(Area)
admin.site.register(YapoUser)
admin.site.register(Provider)
admin.site.register(PurchaseOrder)
