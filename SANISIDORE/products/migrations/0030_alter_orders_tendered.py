# Generated by Django 4.0.2 on 2023-03-31 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_orders_tendered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='Tendered',
            field=models.FloatField(null=True),
        ),
    ]
