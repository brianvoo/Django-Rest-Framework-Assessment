# Generated by Django 4.1.7 on 2023-03-24 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='driver_added',
            field=models.DateField(auto_now_add=True, verbose_name='Driver Added'),
        ),
        migrations.AlterField(
            model_name='truck',
            name='truck_added',
            field=models.DateField(auto_now_add=True, verbose_name='Truck Added'),
        ),
    ]
