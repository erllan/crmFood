# Generated by Django 3.0.2 on 2020-12-09 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0013_auto_20201209_1601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordermeal',
            old_name='table',
            new_name='order',
        ),
    ]