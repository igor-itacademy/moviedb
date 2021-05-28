from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.views import PasswordResetView
from unittest import skip
from django.contrib.auth.models import User
from .models import Profile
from .views import list_movies, activation_page



class URLTests(TestCase):
	def test_list_movies(self):
		url = reverse('list_movies')
		# self.assertEqual(resolve(url).func.__name__, Class_based_view.as_view().__name__ )
		# self.assertEqual(resolve(url).func.view_class, Class_based_view )
		self.assertEqual(resolve(url).func, list_movies )

	@skip
	def test_login_page(self):
		pass


	def test_password_recovery_page(self):
		url = reverse('password_reset')
		self.assertEqual(resolve(url).func.view_class, PasswordResetView )

	def test_activation_page(self):
		url = reverse('activation_page', args=['uid', 'token'])
		self.assertEqual(resolve(url).func, activation_page)


class TestViews(TestCase):
	def setUp(self):
		self.client = Client()

	def test_users_list(self):
		url = reverse('users_list')
		response = self.client.get(url)

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'users/user_list.html')

	# test fails 
	def test_edit_profile_POST(self):
		user = User.objects.create_user(username='uniqueusername',
			email='unique@mail.com',
			password='somepassword123')
		profile = Profile.objects.create(user=user)

		url = reverse('edit_profile')
		data = {'bio': 'hello'}
		self.client.login(username=user.username, password='somepassword123')
		response = self.client.post(url, data)
		self.assertEqual(response.status_code, 302)
		self.assertEqual(profile.bio, 'hello')

