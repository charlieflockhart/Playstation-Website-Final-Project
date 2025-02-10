from . import views
from django.urls import path

urlpatterns = [
    path('', views.ProfileDetailedView.as_view(), name='profile'),
    path('move_game/<str:title>', views.move_game_to_chosen, name='move_game'),
    path('check_game_purchased/<str:title>', views.check_game_ownership, name='check_game_purchased'),
]