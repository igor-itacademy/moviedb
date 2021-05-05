from django.urls import path
from .views import *

urlpatterns = [
	path('register/', registration_page, name='registration_page'),
	path('register2/', second_registration_page, name='second_registration_page'),
	path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
    path('users_list', users_list, name='users_list'),
    path('', list_movies, name='list_movies'),
]
