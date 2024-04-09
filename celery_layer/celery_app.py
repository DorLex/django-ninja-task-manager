import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('celery_app_name')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_notification_periodic': {
        'task': 'tasks.tasks.send_notification',
        'schedule': crontab(minute='*/1'),
        'args': ('OK',)
    },
}
