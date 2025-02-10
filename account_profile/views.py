from django.shortcuts import render, get_object_or_404
from .models import Profile, Game
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# def about_me(request):
    
    
            
#     """
#     Renders the Profile page
#     """
#     profile = Profile.objects.all().order_by('-updated_on').first()


#     return render(
#         request,
#         "account_profile/account_profile.html",
#         {"profile": profile
#         },
#     )

class ProfileDetailedView(DetailView, LoginRequiredMixin):
    model = Profile
    template_name = "account_profile/account_profile.html"
    context_object_name = "profile"


    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user)

@csrf_exempt
def move_game_to_chosen(request, game_title):
    print(f"move_game_to_chosen triggered for game: {game_title}")
    if request.method == 'POST':
        user = request.user
        profile = get_object_or_404(Profile, user=user)
        game = get_object_or_404(Game, title=game_title)

        if game in profile.available_purchased_games.all():
            profile.available_purchased_games.remove(game)
            profile.chosen_purchased_games.add(game)
            profile.save()
            print(f"this has been added to chosen_purchased_games and saved")

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'}, status=400)