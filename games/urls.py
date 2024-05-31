from django.urls import path
from . import views

urlpatterns = [
    path('leaderboard/<int:game_id>/', views.leaderboard, name='leaderboard'),
    path('user-scores/', views.user_scores, name='user_scores'),
]