from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .models import Profile, Game
from django.http import JsonResponse

# from django.contrib.auth.models import User
# from django.db import models

@login_required
def move_game_to_chosen(request, game_title):
    if request.method == 'POST':
        user = request.user
        profile = get_object_or_404(Profile, user=user)
        game = get_object_or_404(Game, title=game_title)

        if game in profile.available_purchased_games.all():
            profile.available_purchased_games.remove(game)
            profile.chosen_purchased_games.add(game)
            profile.save()

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'}, status=400)