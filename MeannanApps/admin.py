from django.contrib import admin
from .models import (
    HomeProducts,
    BillingAddress,
    ContactUs,
    ShippingAddress,
    Order,
    Category,
    Shop
)

# Register your models here.

admin.site.register(HomeProducts)
admin.site.register(Category)
admin.site.register(Shop)
admin.site.register(BillingAddress)
admin.site.register(ContactUs)
admin.site.register(ShippingAddress)
admin.site.register(Order)