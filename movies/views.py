from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from .forms import ContactUsForm


def users_list(request):
	all_users = User.objects.all()
	context = {
		'all_users': all_users
	}
	return render(request, 'users/user_list.html', context)


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
