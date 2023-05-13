# Generated by Django 4.0.2 on 2023-05-13 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_orders_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlines',
            name='Finalprice',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='orderlines',
            name='ProductCost',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='orders',
            name='OrderTotal',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='Tendered',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ProductCost',
            field=models.DecimalField(decimal_places=2, max_digits=10, max_length=6),
        ),
    ]
