# Generated by Django 2.2.4 on 2020-09-22 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0012_auto_20200923_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(default='', max_length=7),
        ),
    ]