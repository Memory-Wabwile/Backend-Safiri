# Generated by Django 4.0.4 on 2022-05-06 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_remove_busbooking_bus_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
    ]