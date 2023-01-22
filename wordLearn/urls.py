from django.urls import path
from .views import home_view, rnd_view

urlpatterns = [
    path('', home_view, name='home-view'),
    path('rnd/', rnd_view, name='rnd-view'),
]