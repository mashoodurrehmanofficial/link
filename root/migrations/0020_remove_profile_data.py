# Generated by Django 3.1.1 on 2020-09-24 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0019_auto_20200924_0843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='data',
        ),
    ]
