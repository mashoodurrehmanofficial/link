# Generated by Django 3.1.1 on 2020-10-01 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0062_profile_packet_creation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='packet_creation_time',
            field=models.IntegerField(default=0),
        ),
    ]
