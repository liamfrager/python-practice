# Generated by Django 4.2.11 on 2024-05-23 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merch_shop', '0019_product_preview_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size_prices',
            field=models.CharField(default='0', max_length=10),
        ),
    ]