from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views 


urlpatterns = [
	path('register/', registration_page, name='registration_page'),
	path('register2/', second_registration_page, name='second_registration_page'),
	path('activate/<uid>/<token>/', activation_page, name='activation_page'),
	path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
    path('user_comments/', user_comments, name='user_comments'),
    path('users_list/', users_list, name='users_list'),
    path('contact_page/', contact_page, name='contact_page'),
    path('', list_movies, name='list_movies'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html', html_email_template_name='users/password_reset_email.html', subject_template_name='users/password_reset_subject.txt'), name = 'password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name = "users/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'users/password_reset_complete.html'), name='password_reset_complete'),
]
