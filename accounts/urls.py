from django.urls import path
from . import views

urlpatterns = [
    path('signup_account/', views.signup_account, name='signup_account'),
    path('logout/', views.logout_account, name='logout_account'),
    path('login/', views.login_account, name='login_account'),
    path('profile/', views.profile, name='profile'),
    path('password/', views.change_password, name='change_password'),
    path('delete/<int:item_id>/', views.profile_delete_rating, name='delete_view'),
]