from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import GameHistory, Leaderboard
from django.utils import timezone

@login_required
def save_game_result(request):
    if request.method == 'POST':
        game_type = request.POST.get('game_type')
        game_settings = request.POST.get('game_settings')
        final_score = request.POST.get('final_score')

        # Save game history
        GameHistory.objects.create(
            user=request.user,
            game_type=game_type,
            game_settings=game_settings,
            final_score=int(final_score)
        )

        # Update leaderboard
        Leaderboard.objects.create(
            user=request.user,
            game_type=game_type,
            final_score=int(final_score)
        )

        return redirect('game_result')

    return redirect('home')

@login_required
def game_history(request):
    history = GameHistory.objects.filter(user=request.user).order_by('-finished_at')
    return render(request, 'game_history.html', {'history': history})

@login_required
def leaderboard(request, game_type):
    leaderboard = Leaderboard.objects.filter(game_type=game_type).order_by('-final_score')[:10]
    return render(request, 'leaderboard.html', {'leaderboard': leaderboard, 'game_type': game_type})
