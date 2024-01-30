from django.urls import path
from . import views
from .views import OrderListView, OrderCreateView, OrderUpdateView, OrderDeleteView, RequisitesListView, RequisitesUpdateView, RequisitesDeleteView, RequisitesCreateView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	path('', OrderListView.as_view(), name='order-list'),
	path('order-create/', OrderCreateView.as_view(), name='order-create'),
	path('order/<int:pk>/update/', OrderUpdateView.as_view(), name='order-update'),
	path('order/<int:pk>/delete/', OrderDeleteView.as_view(), name='order-delete'),
	path('requisites-list/', RequisitesListView.as_view(), name='requisites-list'),
	path('requisites-create/', RequisitesCreateView.as_view(), name='requisites-create'),
	path('requisites/<int:pk>/update/', RequisitesUpdateView.as_view(), name='requisites-update'),
	path('requisites/<int:pk>/delete/', RequisitesDeleteView.as_view(), name='requisites-delete'),
	path('user-roles/', views.user_roles, name='user-roles'),
	path('orders-api/', views.OrderList.as_view(), name='orders-api'),
    path('orders-api/<int:pk>/', views.OrderDetail.as_view(), name='orders-api-detail'),
	path('api/', views.api, name='api'),
]
