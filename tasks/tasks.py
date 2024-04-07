from time import sleep

from celery import shared_task


@shared_task
def send_notification(message):
    sleep(5)
    print(f'Send {message=}')
    
    return message
