# Generated by Django 4.2.3 on 2023-07-31 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("stats", "0003_rename_players_player"),
    ]

    operations = [
        migrations.CreateModel(
            name="Match",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("location", models.CharField(max_length=200)),
                ("opposition", models.CharField(max_length=100)),
                ("date", models.DateField()),
                (
                    "result",
                    models.CharField(
                        choices=[
                            ("W", "Won"),
                            ("L", "Lost"),
                            ("NR", "No_result"),
                            ("T", "Tied"),
                        ],
                        max_length=3,
                    ),
                ),
                ("man_of_match", models.CharField(max_length=20)),
                ("players", models.ManyToManyField(to="stats.player")),
            ],
        ),
        migrations.CreateModel(
            name="Match_Stat",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("runs_scored", models.IntegerField()),
                ("fours", models.IntegerField()),
                ("sixes", models.IntegerField()),
                ("bowls_played", models.IntegerField()),
                ("wickets_taken", models.IntegerField()),
                ("strike_rate", models.FloatField(blank=True, null=True)),
                (
                    "match",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Match_stat",
                        to="stats.match",
                    ),
                ),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Match_stat",
                        to="stats.player",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="OverallStats",
        ),
    ]
