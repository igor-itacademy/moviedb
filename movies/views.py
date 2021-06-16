from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from .forms import ContactUsForm, CommentForm
from .models import Comment, Movie, Profile
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .tasks import add, send_contact_email
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage

def users_list(request):
	
	profiles = Profile.objects.select_related('user')
	# profiles = Profile.objects.all()
	context = {
		'profiles': profiles
	}
	return render(request, 'users/user_list.html', context)


def contact_page(request):
	form = ContactUsForm()
	if request.method == 'POST':
		form = ContactUsForm(request.POST)
		if form.is_valid():
			email_to = form.cleaned_data['email_to']
			sender_name = form.cleaned_data['sender_name']
			# email_template =render_to_string('users/contact_form_email_answer.html', {'sender_name': sender_name})
			# email = EmailMessage(
			# 	'Спасибо за отзыв',
			# 	email_template,
			# 	settings.EMAIL_HOST_USER,
			# 	[email_to],
			# )
			# email.fail_silently=False
			# email.send()
			send_contact_email.delay(email_to, sender_name)
			return redirect('list_movies')
	context = {'form': form}
	return render(request, 'users/contact_page.html', context)


def list_movies(request):
	movies_list = Movie.objects.all()
	paginator = Paginator(movies_list, 1)

	page = request.GET.get('page')

	try:
		movies = paginator.page(page)
	except PageNotAnInteger:
		movies = paginator.page(1)
	except EmptyPage:
		movies = paginator.page(paginator.num_pages)

	# При переходе на эту страницу добавляется фоновая задача
	# add.delay(100, 200)
	context = {'movies': movies}
	return render(request, 'movies/list_movies.html', context)


def movie_detail(request, id):
	movie = Movie.objects.get(id=id)
	# comments = Comment.objects.filter(movie=movie)
	comments = Comment.objects.select_related('user')
	
	context = {
		'movie': movie,
		'comments': comments,
	}
	return render(request, 'movies/movie_detail.html', context)


@login_required(login_url='login_page')
def add_comment(request, id):
	if request.method == 'POST':
		movie = Movie.objects.get(id=id)
		user = request.user
		form = CommentForm(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			if request.POST.get('parent', None):
				form.parent_id = request.POST.get('parent')
			form.movie = movie
			form.user = user
			form.save()

			return redirect(movie. get_absolute_url())

