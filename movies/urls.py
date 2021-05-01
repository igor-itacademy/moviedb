from django.urls import path
from .views import *

urlpatterns = [
	path('register', registration_page, name='registration_page'),
	path('login', login_page, name='login_page'),
    path('', list_movies, name='list_movies'),
]
