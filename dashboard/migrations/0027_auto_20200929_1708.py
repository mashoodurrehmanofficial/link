# Generated by Django 3.1.1 on 2020-09-29 12:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0026_auto_20200929_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentpacket',
            name='packet_creation_time',
            field=models.CharField(default='2020-09-29 17:08:42', max_length=100),
        ),
        migrations.AlterField(
            model_name='uservisitinghistory',
            name='visiting_time',
            field=models.CharField(default=datetime.datetime(2020, 9, 29, 17, 8, 42, 313008), max_length=100),
        ),
    ]
