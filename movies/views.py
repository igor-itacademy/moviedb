from django.shortcuts import render, redirect
from .forms import CreateUserForm, SecondCreateUserForm, LoginForm, ContactUsForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import registration_activation_token
from django.conf import settings


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
			user = form.save(commit=False)
			user.is_active = False
			email_to = user.email
			name = user.username
			user.save()
			email_template =render_to_string('users/confirmation_email.html', 
				{
					'name': name,
					'domain': get_current_site(request).domain,
					'uid': urlsafe_base64_encode(force_bytes(user.pk)),
					'token': registration_activation_token.make_token(user),
				})
			email = EmailMessage(
				'Подтвердите регистрацию',
				email_template,
				settings.EMAIL_HOST_USER,
				[email_to],
			)
			email.content_subtype = 'html'
			email.fail_silently=False
			email.send()
			messages.info(request, "Please valide your email.")
			return redirect(login_page)

	context = {'form': form}
	return render(request, 'movies/registration_page.html', context)


def activation_page(request, uid, token):
	user_id = urlsafe_base64_decode(uid)
	user = User.objects.get(id = user_id)
	if user and registration_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		login(request, user)
		return redirect(list_movies)

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
			email_to = form.cleaned_data['email_to']
			sender_name = form.cleaned_data['sender_name']
			email_template =render_to_string('users/contact_form_email_answer.html', {'sender_name': sender_name})
			email = EmailMessage(
				'Спасибо за отзыв',
				email_template,
				settings.EMAIL_HOST_USER,
				[email_to],
			)
			email.fail_silently=False
			email.send()
			return redirect('list_movies')
	context = {'form': form}
	return render(request, 'users/contact_page.html', context)


def list_movies(request):
	context = {}
	return render(request, 'movies/list_movies.html', context)
