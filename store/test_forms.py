from django.test import TestCase
from store.forms import CommentForm

class CommentFormTest(TestCase):
    def test_comment_form_valid_data(self):
        form = CommentForm(data={
            'title': 'Great Game!',
            'level': 50,
            'rating': 5,
            'platinum_achieved': True,
            'platinum_stability': 0,
            'glitched_trophies': False,
            'glitched_trophies_list': '',
            'game_version': 1.02,
            'playtime': 40,
            'platform': 'PS5',
            'body': 'Really enjoyed this game. Highly recommend!'
        })
        self.assertTrue(form.is_valid())

    def test_comment_form_missing_required_fields(self):
        form = CommentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        self.assertIn('body', form.errors)

    def test_comment_form_invalid_data(self):
        form = CommentForm(data={
            'title': 'Test Title',  
            'level': 10,  # Invalid: Should be an integer  
            'rating': 6,  # Assuming max is 5  
            'platinum_achieved': False,  # Invalid: Should be True/False  
            'platinum_stability': 0,
            'glitched_trophies': False,  # Invalid: Should be True/False  
            'glitched_trophies_list': '',
            'game_version': 1.02,  # Assuming it's a string  
            'playtime': 100,  # Invalid: Should be an integer  
            'platform': 'PS5',  
            'body': 'Test body'  
        })

        print("Form errors:", form.errors)  

        self.assertFalse(form.is_valid())

        # Check that only expected fields have errors  
        self.assertIn('level', form.errors)  # Invalid integer  
        self.assertIn('rating', form.errors)  # Out of range  
        self.assertIn('platinum_achieved', form.errors)  # Invalid boolean  
        self.assertIn('glitched_trophies', form.errors)  # Invalid boolean  
        self.assertIn('playtime', form.errors)  # Invalid integer  


