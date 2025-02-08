# from django.contrib.auth.models import User
# from django.db import models

# def add_test_game_to_user(user_id):
#     print("Adding test game to user with ID:", user_id)
#     try:
#         user = User.objects.get(id=user_id)
#         if hasattr(user, 'games_purchased'):
#             user.games_purchased += 'testing 123'
#             user.save()
#         else:
#             raise AttributeError("User object has no attribute 'games_purchased'")
#     except User.DoesNotExist:
#         raise ValueError("User with the given ID does not exist")