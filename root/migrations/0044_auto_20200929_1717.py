# Generated by Django 3.1.1 on 2020-09-29 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0043_auto_20200929_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='packet_creation_time',
            field=models.CharField(default='2020-09-29 17:17:36', max_length=100),
        ),
    ]