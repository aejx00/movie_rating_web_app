from django.shortcuts import render
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib import messages
from movie.models import Review


def signup_account(request):
    if request.method == 'GET':
        return render(request, 'signup_account.html', 
                    {'form':UserCreateForm})
    elif request.method == 'POST': 
        # validate unique email
        form_sub_email=request.POST['email']
        try:
            db_email = User.objects.get(email__exact=form_sub_email)
        except User.DoesNotExist:
            db_email = None
        if db_email != None:
            if form_sub_email == db_email.email:
                return render(request, 'signup_account.html', 
                        {'form':UserCreateForm,
                        'error':'Account with same email address detected. Please use a different email address.'})
        
        if request.POST['password1'] != request.POST['password2']: 
            # validate password match
            return render(request, 'signup_account.html', 
                {'form':UserCreateForm, 'error':'Passwords do not match'})
        
        try:
            # create user
            user = User.objects.create_user(request.POST['username'],
                            email=request.POST['email'],
                        password=request.POST['password1'])
            user.save()
            login(request, user)
            return redirect('home')
        except IntegrityError: # catch non-unique username
            return render(request, 'signup_account.html', 
                {'form':UserCreateForm,
                'error':'Username already taken. Choose new username.'})
        

def logout_account(request):        
    logout(request)
    return redirect('home')


def login_account(request):    
    if request.method == 'GET':
        return render(request, 'login_account.html', 
                      {'form':AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request,'login_account.html', 
                    {'form': AuthenticationForm(), 
                    'error': 'username and password do not match'})
        else: 
            login(request,user)
            return redirect('home')


def profile(request):    
    if request.method == 'GET':
        profile_reviews = Review.objects.filter( author=request.user)
        return render(request, 'profile.html', 
                      {'form':AuthenticationForm, 'profile_reviews': profile_reviews})
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request,'loginaccount.html', 
                    {'form': AuthenticationForm(), 
                    'error': 'username and password do not match'})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Error chanigng password. Please re-enter according to the guidlines below.')
            return redirect('change_password')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })


def profile_delete_rating(request,item_id =None):
    rating_entry = Review.objects.filter(movie_id=item_id, author=request.user)
    rating_entry.delete()
    profile_reviews = Review.objects.filter( author=request.user)
    return render(request, 'profile.html', 
                      {'form':AuthenticationForm, 'profile_reviews': profile_reviews})