# Generated by Django 4.2.11 on 2024-05-14 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merch_shop', '0011_alter_product_colors_alter_variant_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='colors',
            field=models.ManyToManyField(default=None, to='merch_shop.color'),
        ),
    ]
