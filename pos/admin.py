from django.contrib import admin
from .models import Area, YapoUser, Provider, PurchaseOrder, PurchaseOrderDetail


class DetailInline(admin.StackedInline):
    model = PurchaseOrderDetail
    extra = 3


class PurchaseOrderAdmin(admin.ModelAdmin):
    inlines = [DetailInline]



admin.site.register(Area)
admin.site.register(YapoUser)
admin.site.register(Provider)
admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
