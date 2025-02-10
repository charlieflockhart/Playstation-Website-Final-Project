from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Profile
from store.models import Post

# Profile detailed view
# This view displays the user's profile page
# It displays the user's purchased games
# It also displays the user's profile information
# It is only accessible to logged in users
class ProfileDetailedView(DetailView, LoginRequiredMixin):
    model = Profile
    template_name = "account_profile/account_profile.html"
    context_object_name = "profile"


    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user)

# Function to move a game to the user's purchased games
# This function is called when a user clicks the purchase button
# It adds the game to the user's purchased games
# It also displays a message to the user
# It redirects the user to the game detail page
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


# Function to check if the user owns the game
# This function is called when a user views a game detail page
# It checks if the user owns the game
# It redirects the user to the game detail page

# If the user owns the game, it adds a query parameter to the URL
# The query parameter is used to display a message to the user
# If the user does not own the game, it adds a query parameter to the URL
# The query parameter is used to display a message to the user

# If the user is not logged in, it adds a query parameter to the URL
# The query parameter is used to display a message to the user
# It redirects the user to the game detail page

# The function returns an HTTP response
# The HTTP response contains the URL of the game detail page
# The URL contains the query parameter
# The query parameter is used to display a message to the user
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