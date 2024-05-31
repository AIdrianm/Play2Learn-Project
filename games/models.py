from django.db import models
from django.conf import settings

class Game(models.Model):
    name = models.CharField(max_length=100, default="Game")

    def __str__(self):
        return self.name

class Score(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.game.name} - {self.score}"
