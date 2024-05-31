from django.shortcuts import render
from .models import Game, Score
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def update_score(user_id, game_id, score_value):
    user = User.objects.get(id=user_id)
    game = Game.objects.get(id=game_id)
    score = Score(user=user, game=game, score=score_value)
    score.save()

@login_required
def leaderboard(request, game_id):
    game = Game.objects.get(id=game_id)
    scores = Score.objects.filter(game=game).order_by('-score')[:10]
    context = {
        'game': game,
        'scores': scores
    }
    return render(request, 'leaderboard.html', context)

@login_required
def user_scores(request):
    scores = Score.objects.filter(user=request.user).order_by('-date')
    context = {
        'scores': scores
    }
    return render(request, 'user_scores.html', context)