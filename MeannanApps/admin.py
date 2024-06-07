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

class ShopAdmin(admin.ModelAdmin):
    list_display = ('id','product_name','product_price')
    search_fields = ('product_name',)
    list_filter = ('product_name',)

admin.site.register(Shop, ShopAdmin )
admin.site.register(BillingAddress)
admin.site.register(ContactUs)
admin.site.register(ShippingAddress)
admin.site.register(Order)