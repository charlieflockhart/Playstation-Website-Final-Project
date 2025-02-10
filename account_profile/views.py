from django.shortcuts import render, get_object_or_404
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

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