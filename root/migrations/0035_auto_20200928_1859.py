# Generated by Django 3.1.1 on 2020-09-28 13:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0034_auto_20200928_1845'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='claimable_links',
            new_name='reserved_tokens',
        ),
        migrations.AlterField(
            model_name='profile',
            name='packet_creation_time',
            field=models.CharField(default=datetime.datetime(2020, 9, 28, 18, 59, 50, 717085), max_length=100),
        ),
    ]