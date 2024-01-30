from django.contrib import admin
from .models import Order, Requisites, OrderAdmin, RequisitesAdmin
admin.site.register(Order, OrderAdmin)
admin.site.register(Requisites, RequisitesAdmin)


# Register your models here.
