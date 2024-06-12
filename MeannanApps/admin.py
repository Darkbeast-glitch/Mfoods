from django.contrib import admin
from .models import (
    HomeProducts,
    BillingAddress,
    ContactUs,
    ShippingAddress,
    Order,
    Category,
    Shop,
    ProductVariation,
    Cart,
    CartItem
)

# Register your models here.

admin.site.register(HomeProducts)
admin.site.register(Category)


class ProductVariationInline(admin.TabularInline):
    model = ProductVariation
    extra = 1  # Number of extra empty forms


class ShopAdmin(admin.ModelAdmin):
    inlines = [ProductVariationInline]


# class ShopAdmin(admin.ModelAdmin):
#     list_display = ('id','product_name','product_price')
#     search_fields = ('product_name',)
#     list_filter = ('product_name',)

admin.site.register(Shop, ShopAdmin)
admin.site.register(ProductVariation)
admin.site.register(BillingAddress)
admin.site.register(ContactUs)
admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(CartItem)
admin.site.register(Cart)
