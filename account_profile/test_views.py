from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.messages import get_messages
from account_profile.models import Profile
from store.models import Post
from account_profile.views import ProfileDetailedView, move_game_to_chosen, check_game_ownership

class ProfileDetailedViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.profile = Profile.objects.create(user=self.user)
    
    def test_profile_view_authenticated(self):
        request = self.factory.get(reverse('profile_detail'))
        request.user = self.user
        
        response = ProfileDetailedView.as_view()(request)
        self.assertEqual(response.status_code, 200)
    
    def test_profile_view_unauthenticated(self):
        request = self.factory.get(reverse('profile_detail'))
        request.user = User()
        
        response = ProfileDetailedView.as_view()(request)
        self.assertNotEqual(response.status_code, 200)

class MoveGameToChosenTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.profile = Profile.objects.create(user=self.user)
        self.post = Post.objects.create(title='Test Game', slug='test-game')
    
    def test_move_game_to_chosen(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('move_game_to_chosen', args=['Test Game']))
        
        self.profile.refresh_from_db()
        self.assertIn(self.post, self.profile.purchased_games.all())
        messages = [msg.message for msg in get_messages(response.wsgi_request)]
        self.assertIn("You have purchased the game: Test Game", messages)
    
    def test_move_game_already_purchased(self):
        self.profile.purchased_games.add(self.post)
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('move_game_to_chosen', args=['Test Game']))
        
        messages = [msg.message for msg in get_messages(response.wsgi_request)]
        self.assertIn("You have already purchased the game: Test Game", messages)

class CheckGameOwnershipTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.profile = Profile.objects.create(user=self.user)
        self.post = Post.objects.create(title='Test Game', slug='test-game')
    
    def test_check_ownership_owned(self):
        self.profile.purchased_games.add(self.post)
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('check_game_ownership', args=['Test Game']))
        
        self.assertRedirects(response, f"{reverse('post_detail', kwargs={'slug': self.post.slug})}?purchased=true")
    
    def test_check_ownership_not_owned(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('check_game_ownership', args=['Test Game']))
        
        self.assertRedirects(response, f"{reverse('post_detail', kwargs={'slug': self.post.slug})}?purchased=false")
    
    def test_check_ownership_not_authenticated(self):
        response = self.client.get(reverse('check_game_ownership', args=['Test Game']))
        
        self.assertRedirects(response, f"{reverse('post_detail', kwargs={'slug': self.post.slug})}?purchased=false")
