from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from .models import Requisites, Order
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from functools import reduce
import operator
from django.db.models import Q
from django.contrib.auth.models import User
from rest_framework import generics
from . import serializers

class OrderListView(ListView):
    model = Order
    context_object_name = 'orders'
    paginate_by = 100
    template_name = 'shop/order_list.html'

    def get_context_data(self, **kwargs):
        context = super(OrderListView, self).get_context_data(**kwargs)
        context['title'] = 'Список всех заявок'
        return context

    def get_ordering(self):
        ordering = self.request.GET.get('orderby')
        return ordering

    def get_queryset(self):
        result_search = super(OrderListView, self).get_queryset()
        query = self.request.GET.get('poisk')
        if query:
            query_list = query.split()
            result_search = result_search.filter(
                reduce(operator.and_,
                        (Q(id__icontains=poisk) for poisk in query_list))
            )
        return result_search

class OrderCreateView(CreateView):
    model = Order
    fields = ['summa', 'requisite', 'status']

    success_url = 'http://127.0.0.1:8000/'


class OrderUpdateView(UpdateView):
    model = Order
    fields = ['summa', 'requisite', 'status']

    def get_context_data(self, **kwargs):
        context = super(OrderUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Изменить заявку'
        return context

    success_url = 'http://127.0.0.1:8000/'

class OrderDeleteView(DeleteView):
    model = Order
    success_url = 'http://127.0.0.1:8000/'


class RequisitesListView(ListView):
    model = Requisites
    context_object_name = 'reqs'
    paginate_by = 50
    template_name = 'shop/requisites_list.html'

    def get_context_data(self, **kwargs):
        context = super(RequisitesListView, self).get_context_data(**kwargs)
        context['title'] = 'Список всех реквезитов'
        return context

    def get_ordering(self):
        ordering = self.request.GET.get('orderby')
        return ordering

    def get_queryset(self):
        result_search = super(RequisitesListView, self).get_queryset()
        query = self.request.GET.get('poisk')
        if query:
            query_list = query.split()
            result_search = result_search.filter(
                reduce(operator.and_,
                       (Q(phone__icontains=poisk) for poisk in query_list)) |
                reduce(operator.and_,
                        (Q(fio__icontains=poisk) for poisk in query_list))
            )
        return result_search

class RequisitesCreateView(CreateView):
    model = Requisites
    fields = ['fio', 'phone', 'type_paid', 'type_card_account', 'limit']

    success_url = 'http://127.0.0.1:8000/requisites-list'

class RequisitesUpdateView(UpdateView):
    model = Requisites
    fields = ['fio', 'phone', 'type_paid', 'type_card_account', 'limit']

    def get_context_data(self, **kwargs):
        context = super(RequisitesUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Изменить реквизит'
        return context

    success_url = 'http://127.0.0.1:8000/requisites-list'

class RequisitesDeleteView(DeleteView):
    model = Requisites
    success_url = 'http://127.0.0.1:8000/requisites-list'


def user_roles(request):
    user_site = User.objects.all()
    context = {'users': user_site}
    return render(request, 'shop/user_roles.html', context=context)


def api(request):
    if request.POST.get('api_order'):
        id = request.POST.get('api_order')
        return HttpResponseRedirect(f'http://127.0.0.1:8000/orders-api/{id}')
    else:
        return render(request, 'shop/api.html')

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer