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


class ProductVariation(models.Model):
    product = models.ForeignKey(Shop, on_delete=models.CASCADE)
    weight = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product.product_name} - {self.weight}"


class BillingAddress(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    emailaddress = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone = models.IntegerField()

    class Meta:
        verbose_name = "Billing Address"
        verbose_name_plural = "Billing Addresses"

    def __str__(self) -> str:
        return f"{self.name }"


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
    products = models.ForeignKey(HomeProducts, on_delete=models.CASCADE)
    client = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

        def __str__(self):
            return f"{self.products,self.client}"
