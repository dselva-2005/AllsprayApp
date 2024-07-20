from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib import admin

# Create your models here.

class ProductsModel(models.Model):

    PRODUCT_TYPE = TRANSACTION_TYPES = [
        ('BALL', 'BALL'),
        ('GUN', 'GUN'),
    ]

    name = models.CharField(max_length=30,unique=True)
    timpstamp = models.DateField(auto_now_add=True)
    instock = models.IntegerField()
    size = models.CharField(max_length=15)
    type = models.CharField(max_length=10,choices=PRODUCT_TYPE)
    description = models.TextField()

    def __str__(self):
        return self.name


class ClientsModel(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254,unique=True)
    mobile_no = PhoneNumberField()
    gst_no = models.CharField(max_length=20)
    address = models.TextField()
    


    def __str__(self):
        return self.name


class OrderModel(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey("backend.ProductsModel", on_delete=models.CASCADE,null=False,default=None)
    quantity = models.IntegerField()
    price_per_PSC = models.DecimalField(max_digits=15, decimal_places=2)
    invoice_no = models.ForeignKey("backend.InvoiceModel", on_delete=models.CASCADE,unique=False,null=False)


class InvoiceModel(models.Model):
    buyer_id = models.ForeignKey("backend.ClientsModel", on_delete=models.CASCADE,unique=False)

    def __str__(self):
        return str(self.id)


class OrderXClientModel(models.Model):
    order_no = models.ForeignKey("backend.InvoiceModel", on_delete=models.CASCADE)
    invoice_no = models.ForeignKey("backend.OrderModel", on_delete=models.CASCADE,unique=False)


class LedgerModel(models.Model):
    TRANSACTION_TYPES = [
        ('CREDIT', 'Credit'),
        ('DEBIT', 'Debit'),
    ]

    client = models.ForeignKey("backend.ClientsModel", on_delete=models.CASCADE,null=False,default=None)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)
    transaction_type = models.CharField(max_length=6, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

admin.site.register(ProductsModel)
admin.site.register(ClientsModel)
admin.site.register(InvoiceModel)
admin.site.register(LedgerModel)
