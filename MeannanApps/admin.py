from django.contrib import admin
from .models import Products, BillingAddress,ContactUs,ShippingAddress,Order

# Register your models here.

admin.site.register(Products)
admin.site.register(BillingAddress)
admin.site.register(ContactUs)
admin.site.register(ShippingAddress)
admin.site.register(Order)