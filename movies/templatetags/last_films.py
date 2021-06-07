from django import template
from movies.models import Movie
from django.shortcuts import render

register = template.Library()


@register.inclusion_tag('last_films.html')
def last_three_films():
	movies = Movie.objects.order_by('id')[:3]
	context = {'movies':movies}
	return context