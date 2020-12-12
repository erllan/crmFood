# Generated by Django 3.0.2 on 2020-12-10 14:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0023_auto_20201210_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='data',
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 10, 20, 23, 1, 603676), null=True),
        ),
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 10, 20, 23, 1, 604676), null=True)),
                ('orderid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_api.Order')),
            ],
        ),
    ]