# Generated by Django 4.0.3 on 2022-03-10 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReservationApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationdetails',
            name='confirmation_num',
            field=models.IntegerField(default=1000),
        ),
    ]
