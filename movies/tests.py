from django.test import TestCase
from django.urls import reverse, resolve
from .views import list_movies
from django.contrib.auth.views import PasswordResetView


class URLTests(TestCase):
	def test_list_movies(self):
		url = reverse('list_movies')
		# self.assertEqual(resolve(url).func.__name__, Class_based_view.as_view().__name__ )
		# self.assertEqual(resolve(url).func.view_class, Class_based_view )
		self.assertEqual(resolve(url).func, list_movies )


	def test_login_page(self):
		pass


	def test_password_recovery_page(self):
		url = reverse('password_reset')
		self.assertEqual(resolve(url).func.view_class, PasswordResetView )

