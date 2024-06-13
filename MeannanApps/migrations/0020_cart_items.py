# Generated by Django 4.2.3 on 2024-06-13 12:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("MeannanApps", "0019_remove_order_client_remove_order_products_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="items",
            field=models.ManyToManyField(
                related_name="carts", to="MeannanApps.cartitem"
            ),
        ),
    ]