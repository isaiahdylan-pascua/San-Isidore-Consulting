# Generated by Django 4.0.2 on 2023-03-28 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_alter_orderlines_orderid_alter_orderlines_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlines',
            name='Finalprice',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderlines',
            name='ProductCost',
            field=models.FloatField(default='0'),
            preserve_default=False,
        ),
    ]
