from django.shortcuts import render, redirect
from .forms import CreateUserForm, SecondCreateUserForm, LoginForm, ContactUsForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def users_list(request):
	all_users = User.objects.all()
	context = {
		'all_users': all_users
	}
	return render(request, 'users/user_list.html', context)


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


@login_required(login_url='login_page')
def user_comments(request):
	context = {}
	return render(request, 'users/user_comments.html', context)

def contact_page(request):
	form = ContactUsForm()
	if request.method == 'POST':
		form = ContactUsForm(request.POST)
		if form.is_valid():
			sender_email = form.cleaned_data['sender_email']
			sender_name = form.cleaned_data['sender_name']
			email_template =render_to_string('users/contact_form_email_answer.html', {'sender_name': sender_name})
			email = EmailMessage(
				'Спасибо за отзыв',
				email_template,
				'from@example.com',
				[sender_email],
			)
			email.fail_silently=False
			email.send()
			return redirect('list_movies')
	context = {'form': form}
	return render(request, 'users/contact_page.html', context)


def list_movies(request):
	context = {}
	return render(request, 'movies/list_movies.html', context)


