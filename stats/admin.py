from django.contrib import admin
from .models import *

# Register your models here.
class Match_stat_admin_view(admin.ModelAdmin):
    list_display = ('match','player','runs_scored')
    
class Match_admin_view(admin.ModelAdmin):
    list_display = ('opposition','date')

class player_admin_view(admin.ModelAdmin):
    list_display = ('name','role','shirt_No')

admin.site.register(player,player_admin_view)
admin.site.register(player_stat)
admin.site.register(Match,Match_admin_view)
admin.site.register(Match_Stat ,Match_stat_admin_view)
