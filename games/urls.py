from django.urls import path
from . import views

urlpatterns = [
    # existing paths
    path('save_game_result/', views.save_game_result, name='save_game_result'),
    path('game_history/', views.game_history, name='game_history'),
    path('leaderboard/<str:game_type>/', views.leaderboard, name='leaderboard'),
]
