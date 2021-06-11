from celery import shared_task
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.conf import settings
from .tokens import registration_activation_token


@shared_task
def send_activation_email(username, user_pk, user_email, token, domain):
	email_template =render_to_string('users/confirmation_email.html', 
		{
			'name': username,
			'domain': domain,
			'uid': user_pk,
			'token': token,
		})
	email = EmailMessage(
		'Подтвердите регистрацию',
		email_template,
		settings.EMAIL_HOST_USER,
		[user_email],
	)
	email.content_subtype = 'html'
	# email.fail_silently=False
	email.send()