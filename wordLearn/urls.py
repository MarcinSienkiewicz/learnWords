from django.urls import path
from .views import home_view, rnd_view, guess_view, choose_view

urlpatterns = [
    path('', home_view, name='home-view'),
    path('rnd/', rnd_view, name='rnd-view'),
    path('guess/', guess_view, name='guess-word-view'),
    path('choose/', choose_view, name='choose-what'),
]