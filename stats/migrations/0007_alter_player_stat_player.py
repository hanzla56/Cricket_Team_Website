# Generated by Django 4.2.3 on 2023-07-31 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("stats", "0006_rename_bowls_played_match_stat_balls_played_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player_stat",
            name="player",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="player_stat",
                to="stats.player",
            ),
        ),
    ]