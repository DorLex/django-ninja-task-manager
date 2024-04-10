import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('celery_app_name')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_notification_for_all_users_periodic': {
        'task': 'tasks.tasks.send_notification_for_all_users',
        'args': ('Рассылка', 'У Вас есть новые задачи!'),
        'schedule': crontab(hour='8', minute='0', day_of_week='1'),
    },
}
