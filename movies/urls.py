from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import  static

urlpatterns = [
    path('users_list/', users_list, name='users_list'),
    path('contact_page/', contact_page, name='contact_page'),
    path('', list_movies, name='list_movies'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)