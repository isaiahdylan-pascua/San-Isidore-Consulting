# Generated by Django 4.0.2 on 2023-03-31 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_orderlines_finalprice_orderlines_productcost'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlines',
            name='ProductDesc',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
