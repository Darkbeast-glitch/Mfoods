# Generated by Django 4.2.3 on 2024-06-12 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("MeannanApps", "0013_cart_cartitem"),
    ]

    operations = [
        migrations.AddField(
            model_name="cartitem",
            name="product_variant",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="MeannanApps.productvariation",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="cartitem",
            name="quantity",
            field=models.IntegerField(default=1),
        ),
    ]
