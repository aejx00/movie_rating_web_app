from django.test import TestCase
from movie.models import Review
from django.utils import timezone
from django.contrib.auth.models import User


class TestModels(TestCase):
    def create_rating(self, rating=5, content="Great story, poor acting", author="", movie_id=603, movie_title="The Matrix", movie_img="/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg"):
        self.test_user = User.objects.create_user(username='testuser', password='12345')
        return Review.objects.create(rating = rating, content = content, date_added = timezone.now(), author = self.test_user, movie_id = movie_id, movie_title = movie_title, movie_img = movie_img)

    
    def test_rating_creation(self):
        r = self.create_rating()
        self.assertTrue(isinstance(r, Review))
        self.assertEqual(r.__str__(), r.movie_title)
    

    def tearDown(self):
        self.test_user.delete()
