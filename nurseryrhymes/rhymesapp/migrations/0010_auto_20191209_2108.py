# Generated by Django 2.2.4 on 2019-12-10 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rhymesapp', '0009_rhyme_premium'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rhyme',
            name='premium',
            field=models.BooleanField(default=False),
        ),
    ]
