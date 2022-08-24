from django.shortcuts import render
from django.http import HttpResponse
from .tmdb_services import *
import asyncio
from .forms import ReviewForm
from .models import Review



def home(request):
    url = sync_get_trending('movie')
    if not url.ok :
        return render(request, 'home.html')
    searchTerm = request.GET.get('searchMovie')
    return render(request, 'home.html', {'searchTerm': searchTerm, 'trending':url.json()})


def about(request):
    if request.method == 'GET':
        return render(request, 'about.html')


def terms(request):
    if request.method == 'GET':
        return render(request, 'terms.html')


def privacy(request):
    if request.method == 'GET':
        return render(request, 'privacy.html')


def dynamic_details(request, id):
    url = sync_get_info(id)
    review_items = Review.objects.filter(movie_id=id)
    if request.method == 'GET':
        return render(request, 'details.html', {'API':url.json(), 'form':ReviewForm, 'user_reviews': review_items})
    elif request.method == 'POST':
        review_submission = Review(rating=request.POST['rating'], content=request.POST['content'], movie_id=id, movie_title=url.json()["title"], movie_img=url.json()["poster_path"], author=request.user)
        entry_check = Review.objects.filter(movie_id=id, author=request.user)
        if 0.0 <= float(request.POST['rating']) <= 10.0:
            if entry_check.exists():
                entry_check.update(rating=request.POST['rating'], content=request.POST['content'], movie_id=id, movie_title=url.json()["title"], movie_img=url.json()["poster_path"], author=request.user)
            else:
                review_submission.save()
            return render(request, 'details.html', {'API':url.json(), 'form':ReviewForm, 'user_reviews': review_items})
        else:
            return render(request, 'details.html', {'API':url.json(), 'form':ReviewForm, 'user_reviews': review_items,'error':'Rating must be a float value 0.0-10.0'})


def display(request):
    API = request.GET.get('API')
    payload = sync_get_movies(API)
    return render(request, 'display.html', {'API':payload.json()["results"]})


def delete_rating(request, media_id=None):
    rating_entry = Review.objects.filter(movie_id=media_id, author=request.user)
    rating_entry.delete()
    return render(request, 'profile.html')