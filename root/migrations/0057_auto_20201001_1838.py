# Generated by Django 3.1.1 on 2020-10-01 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0056_auto_20201001_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='packet_creation_time',
            field=models.CharField(default='2020-10-01 18:38:48', max_length=100),
        ),
    ]