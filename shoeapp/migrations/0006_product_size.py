# Generated by Django 3.0.7 on 2020-06-21 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoeapp', '0005_booking_bookingaddress_bookingitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.IntegerField(default=3),
        ),
    ]
