# Generated by Django 3.0.2 on 2020-12-06 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0007_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicePercentage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
