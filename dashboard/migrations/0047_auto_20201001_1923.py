# Generated by Django 3.1.1 on 2020-10-01 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0046_auto_20201001_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claimtank',
            name='submittion_time',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
