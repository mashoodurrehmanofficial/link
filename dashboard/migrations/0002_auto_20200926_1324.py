# Generated by Django 3.1.1 on 2020-09-26 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentpacket',
            name='packetlength',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]