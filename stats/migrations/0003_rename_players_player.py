# Generated by Django 4.2.3 on 2023-07-20 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("stats", "0002_alter_overallstats_options_alter_players_options"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="players",
            new_name="player",
        ),
    ]
