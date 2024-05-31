from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Game, Score

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'score', 'date')
