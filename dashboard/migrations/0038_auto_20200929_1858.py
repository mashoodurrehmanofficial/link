# Generated by Django 3.1.1 on 2020-09-29 13:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0037_auto_20200929_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentpacket',
            name='packet_creation_time',
            field=models.CharField(default='2020-09-29 18:58:43', max_length=100),
        ),
        migrations.AlterField(
            model_name='uservisitinghistory',
            name='visiting_time',
            field=models.CharField(default=datetime.datetime(2020, 9, 29, 18, 58, 43, 198128), max_length=100),
        ),
    ]