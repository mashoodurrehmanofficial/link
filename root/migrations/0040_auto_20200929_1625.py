# Generated by Django 3.1.1 on 2020-09-29 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0039_auto_20200929_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='packet_creation_time',
            field=models.CharField(default='2020-09-29 16:25:10', max_length=100),
        ),
    ]