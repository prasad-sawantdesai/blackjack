from django.conf.urls import url, include
from django.contrib import admin
from blackjack import views

urlpatterns = [
    url(r'^all/$', views.games, name='views_games'),
    url(r'^start_game/$', views.start_game, name='views_start_game'),
    url(r'^play_game/$', views.play_game, name='views_play_game'),
    url(r'^pick_card/$', views.pick_card, name='views_pick_card'),
    url(r'^skip/$', views.skip, name='views_skip'),
]