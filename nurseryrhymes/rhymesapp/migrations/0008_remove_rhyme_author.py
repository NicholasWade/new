# Generated by Django 2.2.4 on 2019-12-07 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rhymesapp', '0007_auto_20191206_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rhyme',
            name='author',
        ),
    ]
