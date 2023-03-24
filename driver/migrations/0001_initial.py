# Generated by Django 4.1.7 on 2023-03-24 03:39

from django.db import migrations, models
import django.db.models.deletion
import driver.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_plate', models.CharField(max_length=50, unique=True, verbose_name='Number Plate')),
                ('registration_number', models.CharField(max_length=50, unique=True, verbose_name='Registration Number')),
                ('truck_added', models.DateField(auto_now_add=True, verbose_name='Date Added')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driverName', models.CharField(max_length=100, verbose_name='Driver Name')),
                ('mobile_number', models.CharField(max_length=20, verbose_name='Mobile Number')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('district', models.CharField(max_length=50, verbose_name='District')),
                ('language', models.CharField(max_length=50, verbose_name='Language')),
                ('driver_added', models.DateField(auto_now_add=True, verbose_name='Date Added')),
                ('assigned_truck', models.ForeignKey(default=driver.models.get_default_status, on_delete=django.db.models.deletion.SET_DEFAULT, to='driver.truck', verbose_name='Assigned Truck')),
            ],
        ),
    ]
