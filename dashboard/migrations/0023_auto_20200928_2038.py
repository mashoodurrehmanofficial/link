# Generated by Django 3.1.1 on 2020-09-28 15:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0022_auto_20200928_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentpacket',
            name='packet_creation_time',
            field=models.CharField(default=datetime.datetime(2020, 9, 28, 20, 38, 25, 45041), max_length=100),
        ),
        migrations.AlterField(
            model_name='uservisitinghistory',
            name='visiting_time',
            field=models.CharField(default=datetime.datetime(2020, 9, 28, 20, 38, 25, 45041), max_length=100),
        ),
    ]
