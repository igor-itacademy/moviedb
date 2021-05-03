from django.shortcuts import render, redirect
from .forms import CreateUserForm, SecondCreateUserForm, LoginForm
from django.contrib.auth import authenticate, login, logout


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
		form = LoginForm(data =request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username = cd['username'], password = cd['password'])
			if user is not None:
				login(request, user)
				return redirect(list_movies)

	context = {'form': form}
	return render(request, 'movies/login_page.html', context)

def logout_page(request):
	logout(request)
	return redirect('login_page')

def list_movies(request):
	context = {}
	return render(request, 'movies/list_movies.html', context)


