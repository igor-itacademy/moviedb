from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.views import PasswordResetView
from unittest import skip
from django.contrib.auth.models import User
from .models import Profile
from .views import list_movies



class URLTests(TestCase):
	def test_list_movies(self):
		url = reverse('list_movies')
		# self.assertEqual(resolve(url).func.__name__, Class_based_view.as_view().__name__ )
		# self.assertEqual(resolve(url).func.view_class, Class_based_view )
		self.assertEqual(resolve(url).func, list_movies )

class TestViews(TestCase):
	def setUp(self):
		self.client = Client()

	def test_users_list(self):
		url = reverse('users_list')
		response = self.client.get(url)

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'users/user_list.html')

