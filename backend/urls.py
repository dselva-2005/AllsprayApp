from django.urls import path,include
from .views import *

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('addproduct/',ProductsView.as_view(),name='products_add'),
    path('allproducts/',ProductsListView.as_view(),name='products_list'),
    path('addclient/',ClientsView.as_view(),name='clients_add'),
    path('allclients/',ClientsListView.as_view(),name='clients_list'),
    path('addledger/',LedgerView.as_view(),name='ledger_add'),
    path('allledger/',LedgerListView.as_view(),name='ledger_list'),
    path('allorders/',OrderListView.as_view(),name='invoice_list'),
    path('backlogout/',backendlogout,name='backlogout'),
    path('makeinvoice/',FormSetView.as_view(),name='formset'),
    path('getinvoice/<int:id>',GenInvoice.as_view(),name='getinvoice'),

]