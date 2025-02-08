from django.shortcuts import render
from .models import Profile


def about_me(request):
    
    
            
    """
    Renders the Profile page
    """
    profile = Profile.objects.all().order_by('-updated_on').first()


    return render(
        request,
        "account_profile/account_profile.html",
        {"profile": profile
        },
    )