# Generated by Django 3.1.3 on 2020-12-03 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("snakeAndLadder", "0002_snl_last_check"),
    ]

    operations = [
        migrations.AddField(
            model_name="snl",
            name="player_no",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
