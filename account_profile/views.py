from django.shortcuts import render, get_object_or_404
from .models import Profile
from store.models import Post
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
def move_game_to_chosen(request, title):
    print(f"move_game_to_chosen triggered for game: {title}")
    if request.method == 'POST':
        user = request.user
        profile = get_object_or_404(Profile, user=user)
        post = get_object_or_404(Post, title=title)

        if post in profile.purchased_games.all():
            profile.purchased_games.remove(post)
            profile.save()
            print(f"this has been added to chosen_purchased_games and saved")
        else:
            profile.purchased_games.add(post)
            profile.save()
            print(f"this has been added to chosen_purchased_games and saved")

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'}, status=400)