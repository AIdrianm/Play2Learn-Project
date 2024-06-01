from django.contrib import admin
from .models import GameHistory, Leaderboard

# Register the new models
admin.site.register(GameHistory)
admin.site.register(Leaderboard)
