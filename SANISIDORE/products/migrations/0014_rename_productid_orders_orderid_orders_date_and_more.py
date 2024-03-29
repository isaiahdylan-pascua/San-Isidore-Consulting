# Generated by Django 4.0.2 on 2023-03-23 08:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_rename_order_orders'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='ProductID',
            new_name='OrderID',
        ),
        migrations.AddField(
            model_name='orders',
            name='Date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='PWDS',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='PaymentOption',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orders',
            name='Table',
            field=models.CharField(max_length=30),
        ),
    ]
