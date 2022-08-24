from django.test import SimpleTestCase
from django.urls import reverse, resolve
from movie import tmdb_services
from unittest import mock


class TestTmdbServices(SimpleTestCase):

    @mock.patch('movie.tmdb_services.sync_get_movies', return_value=200)
    def test_get_movies_url(self, tmdb):
        self.assertEqual(tmdb_services.sync_get_movies('matrix'), 200)


    @mock.patch('movie.tmdb_services.sync_get_info', return_value=200)
    def test_get_info_url(self, tmdb):
        self.assertEqual(tmdb_services.sync_get_info(603), 200)
