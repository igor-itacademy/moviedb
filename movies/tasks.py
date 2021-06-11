from celery import shared_task
import time

@shared_task
def add(x, y):
	time.sleep(10)
	return x+y


@shared_task
def send_contact_email(mail_to, sender_name):
	pass