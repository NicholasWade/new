# Generated by Django 2.2.4 on 2019-12-10 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rhymesapp', '0008_remove_rhyme_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='rhyme',
            name='premium',
            field=models.BooleanField(default=True),
        ),
    ]