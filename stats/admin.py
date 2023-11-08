from django.contrib import admin
from .models import *

# Register your models here.
class Match_stat_admin_view(admin.ModelAdmin):
    list_display = ('match','player','runs_scored')
    


admin.site.register(player)
admin.site.register(player_stat)
admin.site.register(Match)
admin.site.register(Match_Stat ,Match_stat_admin_view)
