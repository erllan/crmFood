# Generated by Django 3.0.2 on 2020-12-09 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0012_auto_20201209_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermeal',
            name='table',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_api.Order', verbose_name='OrderMeal'),
        ),
    ]
