# Generated by Django 3.1.1 on 2020-10-01 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0055_auto_20200930_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='packet_creation_time',
            field=models.CharField(default='2020-10-01 07:57:18', max_length=100),
        ),
    ]