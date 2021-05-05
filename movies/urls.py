from django.urls import path
from .views import *

urlpatterns = [
	path('register/', registration_page, name='registration_page'),
	path('register2/', second_registration_page, name='second_registration_page'),
	path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
    path('user_comments/', user_comments, name='user_comments'),
    path('users_list/', users_list, name='users_list'),
    path('test_email/', test_email, name='test_email'),
    path('', list_movies, name='list_movies'),
]
