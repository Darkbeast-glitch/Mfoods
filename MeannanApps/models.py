from django.conf import settings
from django.db import models


class Category (models.Model):
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.category_name


# model for Home Products
class HomeProducts(models.Model):
    product_name = models.CharField(max_length=50, blank=True, null=True)
    product_price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to="products/")
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "HomeProduct"
        verbose_name_plural = "HomeProducts"

    def __str__(self) -> str:
        return f"{self.product_name}, Ghs {self.product_price}"

# model for shop products


# adding product Variation


class Shop(models.Model):
    product_name = models.CharField(max_length=50, blank=True, null=True)
    product_price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to="products/shops/")
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Shop"
        verbose_name_plural = "Shops"
        ordering = ['id']

    def __str__(self) -> str:
        return self.product_name

    @property
    def total_price(self):
        total = sum(item.product.price *
                    item.quantity for item in self.cartitem_set.all())
        return total


class ProductVariation(models.Model):
    product = models.ForeignKey(Shop, on_delete=models.CASCADE)
    weight = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product.product_name} - {self.weight}"


class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    emailaddress = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    town_city = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = "Billing Address"
        verbose_name_plural = "Billing Addresses"

    def __str__(self) -> str:
        return f"{self.first_name, self.last_name}"


# cart model

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField('CartItem', related_name='carts')

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Shop, on_delete=models.CASCADE)
    product_variant = models.ForeignKey(
        ProductVariation, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "CartItem"
        verbose_name_plural = "CartItems"

    def __str__(self):
        return f"{self.product.product_name} - {self.quantity}"

    @property
    def total_price(self):
        return self.product_variant.price * self.quantity


class ContactUs(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.IntegerField()
    message = models.TextField(max_length=500, blank=True, null=True)

    class Meta:

        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"

    def __str__(self) -> str:
        return self.name


class ShippingAddress(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    streetaddress = models.CharField(max_length=200, blank=True, null=True)
    phonenumber = models.IntegerField()
    city = models.CharField(max_length=50, blank=True, null=True)
    stateprovinceregion = models.CharField(
        max_length=200, blank=True, null=True)
    zippostalcode = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Shipping Address"
        verbose_name_plural = "Shipping Addresses"

    def __str__(self):
        return f"{self.name,self.email, self.streetaddress, self.phonenumber}"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    billing_address = models.ForeignKey(
        BillingAddress, on_delete=models.SET_NULL, null=True)
    date_ordered = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"Order {self.id}"

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

        def __str__(self):
            return f"{self.products,self.client}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Shop, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.quantity} of {self.product}"
