# Generated by Django 3.1.1 on 2020-09-28 04:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_auto_20200928_0937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currentpacket',
            name='packetitemremaining',
        ),
        migrations.AlterField(
            model_name='uservisitinghistory',
            name='visiting_time',
            field=models.CharField(default=datetime.datetime(2020, 9, 28, 9, 39, 44, 224701), max_length=100),
        ),
    ]