# Generated by Django 4.0.2 on 2023-05-10 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_orders_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='OrderTotal',
            field=models.FloatField(null=True),
        ),
    ]
