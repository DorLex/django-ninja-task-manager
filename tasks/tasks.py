from celery import shared_task
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

User = get_user_model()


@shared_task
def send_notification(subject: str, message: str, email: str):
    send_mail(
        f'{subject}',
        f'Сообщение: {message}',
        settings.EMAIL_HOST_USER,
        [email]
    )

    return subject, message, email


@shared_task
def send_notification_for_all_users(subject: str, message: str):
    offset = 0
    chunk_size = 200

    while True:
        users_email = User.objects.all()[offset:offset + chunk_size].values_list('email', flat=True)
        if not users_email:
            break

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            users_email
        )

        offset += chunk_size

    return True
