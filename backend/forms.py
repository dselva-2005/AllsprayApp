from django.forms import ModelForm,formset_factory,forms
from django import forms
from .models import *


class ProductForm(ModelForm):
    class Meta:
        model = ProductsModel
        fields = ['name','size','size','instock','type','description']


class ClientForm(ModelForm):
    class Meta:
        model = ClientsModel
        fields = ['name','email','mobile_no','gst_no','address']

class LedgerForm(ModelForm):
    class Meta:
        model = LedgerModel
        fields = ['client','transaction_type','description','amount']


class OrderForm(ModelForm):
    class Meta:
        model = OrderModel
        fields = ['product','quantity','price_per_PSC']


class InvoiceForm(ModelForm):
    class Meta:
        model = InvoiceModel
        fields = ['buyer_id']


product = formset_factory(OrderForm,extra=4)
