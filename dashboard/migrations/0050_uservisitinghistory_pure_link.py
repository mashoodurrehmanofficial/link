# Generated by Django 3.1.1 on 2020-10-02 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0049_auto_20201001_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='uservisitinghistory',
            name='pure_link',
            field=models.URLField(blank=True, max_length=300),
        ),
    ]
