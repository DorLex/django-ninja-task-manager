from time import sleep

from celery import shared_task
from django.contrib.auth import get_user_model

User = get_user_model()


@shared_task
def send_notification(message):
    sleep(3)
    print(f'<Send {message=}>')

    return message


@shared_task
def send_many_notifications():
    offset = 0
    chunk_size = 3

    user_emails = User.objects.all()[offset:offset + chunk_size].values_list('email', flat=True)

    while user_emails:
        print(f'<Send notifications for {user_emails=}>')

        offset += chunk_size
        user_emails = User.objects.all()[offset:offset + chunk_size].values_list('email', flat=True)

    return True
