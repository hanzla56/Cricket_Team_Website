from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# These three lines added manually to manage images in models that uploaded by user or admin
from django.core.files.storage import FileSystemStorage
from django.conf import settings
fs = FileSystemStorage(location=settings.MEDIA_ROOT)
# Create your models here.

class player(models.Model):
     name = models.CharField(max_length=20)
     shirt_No = models.IntegerField(blank=True)
     image = models.ImageField()
     role = models.CharField(max_length=254)


     def __str__(self):
        return self.name
     
     class Meta:
        verbose_name_plural = "players"


class player_stat(models.Model):
    player = models.ForeignKey(player, on_delete=models.CASCADE , related_name='player_stat')
    matches = models.IntegerField()
    innings = models.IntegerField()
    runs = models.IntegerField()
    average = models.FloatField()
    wickets = models.IntegerField()
    balls_played = models.IntegerField()
    sixes = models.IntegerField()
    fours = models.IntegerField()
    strike_Rate = models.FloatField()
    best_Score = models.IntegerField()
    Man_of_Matches = models.IntegerField()
    not_Out = models.IntegerField()
    fifties = models.IntegerField()
    centuries = models.IntegerField
    season = models.CharField(max_length=30)
    

    def __str__(self):
        return self.player.name

class Match(models.Model):
    Result = (
        ('W', 'Won'),
        ('L', 'Lost'),
        ('NR', 'No_result'),
        ('T', 'Tied'),
    )
    players = models.ManyToManyField(player)
    location = models.CharField(max_length=200)
    opposition = models.CharField(max_length=100)
    date = models.DateField()
    result = models.CharField(max_length=3 , choices=Result)
    man_of_match = models.CharField(max_length=20)


    def save(self, *args, **kwargs):
        super(Match, self).save(*args, **kwargs)

        for player in self.players.all():
            # Fetch the corresponding player stat for the player
            try:
                player_stats = player_stat.objects.get(player=player)
            except player_stat.DoesNotExist:
                player_stats = player_stat.objects.create(player=player)

            # Update the player stat for the selected player
            player_stats.matches = Match.objects.filter(players=player).count()
            player_stats.save()

    def __str__(self):
        return f'LPCC vs {self.opposition}'
    
    class Meta:
        verbose_name_plural = "Matches"



class Match_Stat(models.Model):
    match = models.OneToOneField(Match , on_delete=models.CASCADE , related_name='match_stat')
    player = models.ForeignKey(player , on_delete=models.CASCADE , related_name='match_stat')
    runs_scored = models.IntegerField()
    fours = models.IntegerField()
    sixes = models.IntegerField()
    balls_played = models.IntegerField()
    wickets_taken = models.IntegerField()
    strike_rate = models.FloatField(null=True , blank=True)

    def __str__(self):
        return self.player.name


  
# This is the receiver function which is triggerd whenever a new object is create of Match_Stat model
@receiver(post_save, sender=Match_Stat)
def update_player_stats(sender, instance, created, **kwargs):
    if created:
        # Fetch the corresponding player stat for the player in the new MatchStat instance
        try:
            player_stats = player_stat.objects.get(player=instance.player)
        except player_stat.DoesNotExist:
            player_stats = player_stat.objects.create(player=instance.player)

        # Update the player stats based on the new match stat data
        player_stats.innings = sender.objects.filter(player=instance.player, runs_scored__gt=0).count()
        player_stats.runs += instance.runs_scored
        player_stats.average = player_stats.runs / player_stats.innings if player_stats.innings > 0 else 0.0
        player_stats.wickets += instance.wickets_taken
        player_stats.balls_played += instance.balls_played
        player_stats.sixes += instance.sixes
        player_stats.fours += instance.fours
        # Update other player_stat fields as needed

        player_stats.save()










