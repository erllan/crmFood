# Generated by Django 3.0.2 on 2020-12-15 13:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0026_auto_20201215_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 15, 19, 7, 20, 303312), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 15, 19, 7, 20, 302312), null=True),
        ),
    ]