# Generated by Django 3.1.1 on 2020-09-28 04:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_auto_20200928_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uservisitinghistory',
            name='visiting_time',
            field=models.CharField(default=datetime.datetime(2020, 9, 28, 9, 40, 0, 68985), max_length=100),
        ),
    ]