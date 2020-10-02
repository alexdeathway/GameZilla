# Generated by Django 3.0.5 on 2020-10-01 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='background',
        ),
        migrations.AddField(
            model_name='game',
            name='min_player',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='game_url',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
