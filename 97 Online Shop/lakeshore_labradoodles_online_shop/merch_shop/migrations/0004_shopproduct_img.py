# Generated by Django 4.2.11 on 2024-05-04 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merch_shop', '0003_alter_shopproduct_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopproduct',
            name='img',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
