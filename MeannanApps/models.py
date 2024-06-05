from django.db import models

# Create your models here
# creating model for Products

class Products(models.Model):
    product_name = models.CharField (max_length=50, blank=True, null=True)
    product_price = models.FloatField()
    product_image = models.ImageField(upload_to="products/")
    description = models.TextField()
 
    class Meta:
        verbose_name = "Product"
    verbose_name_plural = "Products"

    def __str__(self) -> str:
        return f"{self.product_name}, {self.product_price}"
    
class BillingAddress(models.Model):
        name=models.CharField(max_length=200,blank=True,null=True)
        emailaddress=models.EmailField( blank=True,null=True)
        address=models.CharField(max_length=200,blank=True,null=True)
        phone=models.IntegerField()
        

        class Meta:
            verbose_name= "Billing Address"
            verbose_name_plural= "Billing Addresses"

        def __str__(self) -> str:
                return f"{self.name }"   


class ContactUs(models.Model):
    name=models.CharField(max_length=200, blank=True,null=True)
    email=models.EmailField(blank=True, null=True)
    phone=models.IntegerField()
    subject=models.CharField(max_length=500, blank=True,null=True)
    message=models.CharField(max_length=500, blank=True,null=True)

    class Meta:

        verbose_name="Contact Us"
        verbose_name_plural="Contact Us"

    
    def __str__(self) -> str:
        return f"{self.name, self.email,self.phone}"
    

class ShippingAddress(models.Model):
    name=models.CharField(max_length=200, blank=True,null=True)
    email=models.EmailField(blank=True, null=True)
    streetaddress=models.CharField(max_length=200, blank=True,null=True)
    phonenumber=models.IntegerField()
    city=models.CharField(max_length=50,blank=True,null=True)
    stateprovinceregion=models.CharField(max_length=200, blank=True,null=True)
    zippostalcode=models.CharField(max_length=200, blank=True,null=True)
    country=models.CharField(max_length=200, blank=True,null=True)

    class Meta:
        verbose_name="Shipping Address"
        verbose_name_plural="Shipping Addresses"

    def __str__(self):
        return f"{self.name,self.email, self.streetaddress, self.phonenumber}"
     

class Order(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    client=models.CharField(max_length=200, blank=True,null=True)

    class Meta:
        verbose_name="Order"
        verbose_name_plural="Orders"

        def __str__(self):
            return f"{self.products,self.client}"       