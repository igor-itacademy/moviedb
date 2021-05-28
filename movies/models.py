from django.db import models
from django.contrib.auth.models import User
import os


def user_image_dir(instance, filename):
	return os.path.join('avatars', f'{instance.user.id}', filename)

class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	photo = models.ImageField(upload_to=user_image_dir, blank=True, default='avatars/default.webp')
	bio = models.TextField()

	def __str__(self):
		return self.user.username


class Director(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Movie(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	director = models.ForeignKey(Director, on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class Actor(models.Model):
	name = models.CharField(max_length=50)
	movies = models.ManyToManyField(Movie)

	def __str__(self):
		return self.name

