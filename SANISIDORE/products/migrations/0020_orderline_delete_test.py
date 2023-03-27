# Generated by Django 4.0.2 on 2023-03-27 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_test_productid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orderline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductQty', models.IntegerField()),
                ('Discount', models.CharField(blank=True, max_length=30)),
                ('OrderID', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='products.orders')),
                ('ProductID', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.DeleteModel(
            name='test',
        ),
    ]
