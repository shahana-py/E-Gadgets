# Generated by Django 5.0.6 on 2024-11-21 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_rename_product_ordereditem_product_order_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
