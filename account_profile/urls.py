from . import views
from django.urls import path

urlpatterns = [
    # path('', views.about_me, name='profile'),
    path('', views.ProfileDetailedView.as_view(), name='profile'),
]