# Generated by Django 4.0.2 on 2023-03-27 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_rename_orders_order'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orderline',
            new_name='Orderlines',
        ),
        migrations.RenameModel(
            old_name='Order',
            new_name='Orders',
        ),
    ]
