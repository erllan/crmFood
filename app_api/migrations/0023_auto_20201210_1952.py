# Generated by Django 3.0.2 on 2020-12-10 13:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0022_auto_20201210_1939'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordermeal',
            old_name='name',
            new_name='meal',
        ),
        migrations.AlterField(
            model_name='order',
            name='data',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 10, 19, 52, 51, 553147), null=True),
        ),
    ]
