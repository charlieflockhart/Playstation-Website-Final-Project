from . import views
from django.urls import path

urlpatterns = [
    path('', views.ProfileDetailedView.as_view(), name='profile'),
    path('move_game', views.move_game_to_chosen, name='move_game'),
]