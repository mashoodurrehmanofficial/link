# Generated by Django 3.1.1 on 2020-09-28 06:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0029_profile_currentpacketitemsremaining'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='packet_creation_time',
            field=models.CharField(default=datetime.datetime(2020, 9, 28, 11, 37, 33, 486166), max_length=100),
        ),
    ]
