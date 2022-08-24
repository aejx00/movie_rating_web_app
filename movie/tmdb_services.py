import os
import json
import requests

TMDB_KEY = os.environ.get('TMDB_API_KEY')


def sync_get_movies(title: str) -> str:
    if title is None:
        return None
    try:
        url = "https://api.themoviedb.org/3/search/movie?api_key={}&language=en-US&query={}&page=1&include_adult=false".format(TMDB_KEY, title)
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        return response
    except requests.exceptions.Timeout:
        print ("Timeout Error: ", url)
    except requests.exceptions.TooManyRedirects:
        print ("Too many redirects Error: ", url)
    except requests.exceptions.RequestException as e:
        print ("Error: ", e)


def sync_get_info(id: int) -> str:
    if id is None:
        return None
    try:
        url = "https://api.themoviedb.org/3/movie/{}?language=en-US&api_key={}".format(id, TMDB_KEY)
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        return response
    except requests.exceptions.Timeout:
        print ("Timeout Error: ", url)
    except requests.exceptions.TooManyRedirects:
        print ("Too many redirects Error: ", url)
    except requests.exceptions.RequestException as e:
        print ("Error: ", e)


def sync_get_trending(media_type: str) -> str:
    if media_type is None:
        return None
    try:
        url = "https://api.themoviedb.org/3/trending/{}/day?api_key={}".format(media_type, TMDB_KEY)
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        return response
    except requests.exceptions.Timeout:
        print ("Timeout Error: ", url)
    except requests.exceptions.TooManyRedirects:
        print ("Too many redirects Error: ", url)
    except requests.exceptions.RequestException as e:
        print ("Error: ", e)

