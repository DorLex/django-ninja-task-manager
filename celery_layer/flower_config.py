from django.conf import settings

broker_api = (
    'http://'
    f'{settings.RABBITMQ_DEFAULT_USER}:'
    f'{settings.RABBITMQ_DEFAULT_PASS}@'
    f'{settings.RABBITMQ_HOST}:'
    f'{settings.RABBITMQ_MANAGEMENT_PLUGIN_PORT}'
    '/api/'
)
