from django.shortcuts import render, get_object_or_404
from .models import Profile
from store.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect

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
            messages.error(request, f"You have already purchased the game: {title}")
        else:
            profile.purchased_games.add(post)
            profile.save()
            print(f"this has been added to chosen_purchased_games and saved")
            messages.success(request, f"You have purchased the game: {title}")

    return HttpResponseRedirect(f"{reverse('post_detail', kwargs={'slug': post.slug})}?purchased=true")

@csrf_exempt
def check_game_ownership(request, title):
    post = get_object_or_404(Post, title=title)
    if request.user.is_authenticated:
        print(f"checked this page for {title} ownership")
        user = request.user
        profile = get_object_or_404(Profile, user=user)
        

        if post in profile.purchased_games.all():
            return HttpResponseRedirect(f"{reverse('post_detail', kwargs={'slug': post.slug})}?purchased=true")
        else:
            return HttpResponseRedirect(f"{reverse('post_detail', kwargs={'slug': post.slug})}?purchased=false")
    else:   
        return HttpResponseRedirect(f"{reverse('post_detail', kwargs={'slug': post.slug})}?purchased=false")