# Generated by Django 4.0.2 on 2023-03-23 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_rename_productcost_test_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='test',
            new_name='Order',
        ),
    ]
