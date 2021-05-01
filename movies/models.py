from django.db import models


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

