# Generated by Django 3.0.5 on 2020-09-26 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snakeAndLadder', '0005_auto_20200923_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='snlplayer',
            name='round',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
