# Generated by Django 4.0.2 on 2023-03-23 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='ProductID',
            new_name='OrderID',
        ),
        migrations.RenameField(
            model_name='test',
            old_name='ProductName',
            new_name='Server',
        ),
        migrations.RenameField(
            model_name='test',
            old_name='ProductCost',
            new_name='Table',
        ),
    ]
