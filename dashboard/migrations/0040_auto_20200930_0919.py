# Generated by Django 3.1.1 on 2020-09-30 04:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0039_auto_20200930_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claimtank',
            name='submittion_time',
            field=models.CharField(default='2020-09-30 09:19:26', max_length=100),
        ),
        migrations.AlterField(
            model_name='currentpacket',
            name='packet_creation_time',
            field=models.CharField(default='2020-09-30 09:19:26', max_length=100),
        ),
        migrations.AlterField(
            model_name='uservisitinghistory',
            name='visiting_time',
            field=models.CharField(default=datetime.datetime(2020, 9, 30, 9, 19, 26, 423990), max_length=100),
        ),
    ]