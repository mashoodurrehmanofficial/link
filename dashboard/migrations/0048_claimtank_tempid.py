# Generated by Django 3.1.1 on 2020-10-01 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0047_auto_20201001_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='claimtank',
            name='tempID',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]