from django.db import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class Requisites(models.Model):
    type_paid = models.CharField(max_length=14, blank=False, null=False, choices=((i, i) for i in ('карта', 'платежный счет')))
    type_card_account = models.CharField(max_length=16, blank=False, null=False)
    fio = models.CharField(max_length=64, blank=False, null=False, unique=True)
    phone = models.CharField(max_length=12, blank=False, null=False, unique=True)
    limit = models.CharField(max_length=12, blank=True, null=True, default='0')

    def __str__(self):
        return self.fio+', '+self.phone+', '+self.type_paid+', '+self.type_card_account+', '+self.limit

class Order(models.Model):
    summa = models.FloatField(max_length=16, blank=False, null=False)
    requisite = models.ManyToManyField(Requisites)
    status = models.CharField(max_length=14, blank=False, null=False, choices=((i, i) for i in ('Ожидает оплаты', 'Оплачена', 'Отменена')))

class OrderAdmin(admin.ModelAdmin):
    list_display = ('summa', 'status')
    list_display_links = ('summa', 'status')
    ordering = ['summa', 'status']
    list_filter = ('status',)

class RequisitesAdmin(admin.ModelAdmin):
    list_display = ('type_paid', 'type_card_account', 'fio', 'phone', 'limit')
    list_display_links = ('type_paid', 'type_card_account', 'fio', 'phone', 'limit')
    search_fields = ('type_paid', 'type_card_account', 'fio', 'phone', 'limit')
    ordering = ['type_paid', 'type_card_account', 'fio', 'phone', 'limit']
    list_filter = ('type_paid', 'type_card_account')