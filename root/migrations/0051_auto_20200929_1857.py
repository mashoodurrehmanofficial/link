# Generated by Django 3.1.1 on 2020-09-29 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0050_auto_20200929_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='packet_creation_time',
            field=models.CharField(default='2020-09-29 18:57:01', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='userid',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='website',
            field=models.CharField(default='', max_length=100),
        ),
    ]
