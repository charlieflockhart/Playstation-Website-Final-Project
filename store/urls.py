from . import views
from django.urls import path
from account_profile.views import move_game_to_chosen

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('games/', views.GamesList.as_view(), name='games'),
    path('games_searched/', views.GamesSearchedList.as_view(), name='search'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
    # path('move_game', move_game_to_chosen, name='move_game'),
]