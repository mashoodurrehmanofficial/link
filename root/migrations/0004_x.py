# Generated by Django 2.0 on 2020-09-21 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0003_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='x',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e', models.TextField()),
            ],
        ),
    ]
