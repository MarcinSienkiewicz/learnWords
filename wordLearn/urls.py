from django.urls import path
from .views import (
    home_view, rnd_view,
    choose_view, play_view, result_view)

urlpatterns = [
    path('', home_view, name='home-view'),
    path('rnd/', rnd_view, name='rnd-view'),    
    path('choose/', choose_view, name='choose-what'),
    path('play/', play_view, name='play-game'),
    path('result/', result_view, name='results'),
]