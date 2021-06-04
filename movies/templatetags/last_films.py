from django import template
from movies.models import Movie
from django.shortcuts import render

register = template.Library()


@register.inclusion_tag
def last_three_films():
	films = Movie.objects.order_by('id')[:3]
	context = {'films':films}
	return context