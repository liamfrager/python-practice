# Generated by Django 5.0.4 on 2024-05-04 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merch_shop', '0002_shopproduct_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopproduct',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
