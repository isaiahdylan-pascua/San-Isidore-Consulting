# Generated by Django 4.0.2 on 2023-03-27 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_rename_orderlines_orderline'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]
