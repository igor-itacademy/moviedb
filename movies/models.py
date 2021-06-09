from django.db import models
from django.contrib.auth.models import User
import os
from django.urls import reverse
from PIL import Image


def user_image_dir(instance, filename):
	return os.path.join('avatars', f'{instance.user.id}', filename)

class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	photo = models.ImageField(upload_to=user_image_dir, blank=True, default='avatars/default.webp')
	bio = models.TextField()

	def __str__(self):
		return self.user.username


	# def save(self, *args, **kwargs):
	# 	photo = Image.open(self.photo)
	# 	self.photo = photo.resize(photo, (200, 200))
	# 	super().save(*args, **kwargs)


class Director(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Movie(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	director = models.ForeignKey(Director, on_delete=models.CASCADE)

	def get_absolute_url(self):
		return reverse('movie_detail', kwargs={'id': self.id})
		
	def get_comments(self):
		return self.comment_set.filter(parent__isnull=True)

	def __str__(self):
		return self.name


class Actor(models.Model):
	name = models.CharField(max_length=50)
	movies = models.ManyToManyField(Movie)

	def __str__(self):
		return self.name

class Comment(models.Model):
	text = models.TextField(max_length=500)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
	parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)

	def __str__(self):
		return f'{self.user.username} - {self.movie.name}'

	class Meta:
		verbose_name='Коммент'
		verbose_name_plural='Комменты'