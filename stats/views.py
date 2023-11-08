from django.shortcuts import render
from .models import player, player_stat
# Create your views here.
def players_List(request):
    players = player.objects.all()
    return render(request , 'stats/players.html' , {'players' : players})