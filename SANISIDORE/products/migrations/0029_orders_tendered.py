# Generated by Django 4.0.2 on 2023-03-31 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0028_orderlines_productdesc'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='Tendered',
            field=models.FloatField(default='0'),
            preserve_default=False,
        ),
    ]
