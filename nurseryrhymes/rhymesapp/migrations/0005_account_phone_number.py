# Generated by Django 2.2.4 on 2019-11-14 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rhymesapp', '0004_auto_20191113_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='phone_number',
            field=models.EmailField(default='', max_length=100),
        ),
    ]
