from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, SecondCreateUserForm, LoginForm


def registration_page(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(list_movies)

	context = {'form': form}
	return render(request, 'movies/registration_page.html', context)


def second_registration_page(request):
	form = SecondCreateUserForm()
	if request.method == 'POST':
		form = SecondCreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(list_movies)

	context = {'form': form}
	return render(request, 'movies/registration_2.html', context)


def login_page(request):
	form = LoginForm()
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data

	context = {'form': form}
	return render(request, 'movies/login_page.html', context)


def list_movies(request):
	context = {}
	return render(request, 'movies/list_movies.html', context)


