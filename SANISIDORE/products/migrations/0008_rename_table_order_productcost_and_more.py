# Generated by Django 4.0.2 on 2023-03-23 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_order_date_remove_order_pwds_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Table',
            new_name='ProductCost',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='OrderID',
            new_name='ProductID',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='Server',
            new_name='ProductName',
        ),
    ]
