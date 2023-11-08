from django.contrib import admin
from django.urls import path
from stats import views

app_name = "stats"

urlpatterns = [
    path("" , views.players_List , name='Home_Page'),
]