# Generated by Django 4.0.2 on 2023-03-23 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='ProductID',
        ),
        migrations.AddField(
            model_name='test',
            name='OrderID',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='products.orders'),
        ),
    ]
