# Generated by Django 4.0.2 on 2023-03-23 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_rename_productid_orders_orderid_orders_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductID', models.IntegerField()),
            ],
        ),
    ]
