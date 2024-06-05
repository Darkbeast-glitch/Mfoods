from django.db import models

# Create your models here.
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
        name=models.CharField(max_length=20,blank=True,null=True)
        emailaddress=models.EmailField( max_length=20, blank=True,null=True)
        address=models.CharField(max_length=30,blank=True,null=True)
        phone=models.IntegerField()
        suggestion=models.CharField

        class Meta:
            verbose_name= "Billing Address"
            verbose_name_plural= "Billing Addresses"

        def __str__(self) -> str:
                return f"{self.name }"   
