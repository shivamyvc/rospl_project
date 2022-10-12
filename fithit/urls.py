
from django.http import request
from django.urls import path
from django.urls.conf import include
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    
    path("",views.Home,name='home'),
    path('videos',views.videos,name='videos'),
    path('Signup',views.Signup,name='Login_signup'),
    path('recipe/<str:recipe_id>/', views.view_recipe, name='recipe'),
    path('search',views.filter_video,name='Search'),
    path('search_recipe',views.filter_recipe,name='Search-recipe'),
    path('recipe/<str:recipe_id>/', views.view_recipe, name='recipe'),
    path('Eatbetter',views.Eatbetter,name='Eatbetter'),
    path('about',views.about,name='about'),
    path('register',views.register,name='register'),
    path('login',views.user_login,name='login'),
    path('logout',views.user_logout,name='logout-user'),

    
]
