from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.conf import settings
from .tokens import registration_activation_token
from .forms import CreateUserForm, SecondCreateUserForm, LoginForm,  EditProfileForm
from .decorators import *

from .tasks import send_activation_email

@login_required(login_url='login_page')
def user_comments(request):
	context = {}
	return render(request, 'users/user_comments.html', context)

@for_unauthenticated_user
def registration_page(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False
			user_email = user.email
			user_pk = urlsafe_base64_encode(force_bytes(user.pk))
			username = user.username
			token = registration_activation_token.make_token(user)
			# name = user.username
			user.save()
			domain = get_current_site(request).domain
			send_activation_email.delay(username, user_pk, user_email, token, domain)
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
		return redirect('list_movies')

@for_unauthenticated_user
def second_registration_page(request):
	form = SecondCreateUserForm()
	if request.method == 'POST':
		form = SecondCreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('list_movies')

	context = {'form': form}
	return render(request, 'movies/registration_2.html', context)

@for_unauthenticated_user
def login_page(request):
	form = LoginForm()
	if request.method == 'POST':
		form = LoginForm(data =request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username = cd['username'], password = cd['password'])
			if user is not None:
				login(request, user)
				return redirect('list_movies')

	context = {'form': form}
	return render(request, 'movies/login_page.html', context)


def logout_page(request):
	logout(request)
	return redirect('login_page')


@login_required(login_url='login_page')
def edit_profile(request):
	form = EditProfileForm(instance=request.user.profile)
	if request.method == 'POST':
		form = EditProfileForm(
			request.POST,
			request.FILES,
			instance=request.user.profile)
		if form.is_valid():
			form.save()
			return redirect('list_movies')
			
	context = {'form':form}
	return render(request, 'users/edit_profile.html', context)