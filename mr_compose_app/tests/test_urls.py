from django.test import SimpleTestCase
from django.urls import reverse, resolve
from movie import views as movieViews

class TestUrls(SimpleTestCase):
    

    def test_movie_home_url(self):
        url = reverse('home')
        print(url)
        self.assertEquals(resolve(url).func, movieViews.home)
    

    def test_movie_about_url(self):
        url = reverse('about')
        print(url)
        self.assertEquals(resolve(url).func, movieViews.about)
    

    def test_movie_details_url(self):
        url = reverse('details', args=[603])
        print(url)
        self.assertEquals(resolve(url).func, movieViews.dynamic_details)

    
    def test_movie_display_url(self):
        url = reverse('display')
        print(url)
        self.assertEquals(resolve(url).func, movieViews.display)
    

    
