# Generated by Django 3.0.2 on 2020-12-15 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0028_auto_20201215_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 15, 19, 8, 40, 309888), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 15, 19, 8, 40, 307888), null=True),
        ),
    ]
