# Generated by Django 2.2.4 on 2020-09-21 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0007_delete_x'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='email_verfied',
            new_name='email_verified',
        ),
    ]
