# Generated by Django 3.2.8 on 2021-10-08 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='date_added',
            field=models.DateTimeField(blank=True, max_length=200, null=True),
        ),
    ]
