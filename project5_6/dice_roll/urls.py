from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="dice_home"),
    path('game', views.game, name='game'),
    path('results', views.results, name='results'),
]