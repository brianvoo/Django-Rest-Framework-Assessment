# Generated by Django 4.1.7 on 2023-03-23 13:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0003_alter_driver_assigned_truck'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driver',
            old_name='date_added',
            new_name='driver_added',
        ),
        migrations.AddField(
            model_name='driver',
            name='language',
            field=models.CharField(default='a', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='truck',
            name='truck_added',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]