# Generated by Django 4.2.3 on 2023-07-19 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="players",
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
                ("name", models.CharField(max_length=20)),
                ("shirt_No", models.IntegerField(blank=True)),
                ("image", models.ImageField(upload_to="")),
                ("role", models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name="player_stat",
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
                ("matches", models.IntegerField()),
                ("innings", models.IntegerField()),
                ("runs", models.IntegerField()),
                ("average", models.FloatField()),
                ("wickets", models.IntegerField()),
                ("balls_played", models.IntegerField()),
                ("sixes", models.IntegerField()),
                ("fours", models.IntegerField()),
                ("strike_Rate", models.FloatField()),
                ("best_Score", models.IntegerField()),
                ("Man_of_Matches", models.IntegerField()),
                ("not_Out", models.IntegerField()),
                ("fifties", models.IntegerField()),
                ("season", models.DateField()),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="stats.players"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OverallStats",
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
                ("total_matches", models.IntegerField()),
                ("total_innings", models.IntegerField()),
                ("total_runs", models.IntegerField()),
                ("average", models.FloatField()),
                ("total_wickets", models.IntegerField()),
                ("total_balls_played", models.IntegerField()),
                ("total_sixes", models.IntegerField()),
                ("total_fours", models.IntegerField()),
                ("strike_rate", models.FloatField()),
                ("best_score", models.IntegerField()),
                ("total_man_of_matches", models.IntegerField()),
                ("total_not_out", models.IntegerField()),
                ("total_fifties", models.IntegerField()),
                ("total_centuries", models.IntegerField()),
                (
                    "player",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="stats.players"
                    ),
                ),
            ],
        ),
    ]
