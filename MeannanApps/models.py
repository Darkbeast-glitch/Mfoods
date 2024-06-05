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
