# Generated by Django 4.0.2 on 2023-03-23 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_rename_productname_test_server'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='ProductCost',
            new_name='Table',
        ),
    ]
