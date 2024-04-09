MANAGE = python manage.py
CELERY = celery -A celery_layer.celery_app:app

migrate:
	$(MANAGE) makemigrations
	$(MANAGE) migrate

superuser:
	$(MANAGE) createsuperuser

run:
	uvicorn core.asgi:application --reload

worker_run:
	$(CELERY) worker -l INFO

beat_run:
	$(CELERY) beat -l INFO

flower_run:
	$(CELERY) flower --conf='./celery_layer/flower_config.py'

docker_run:
	docker compose up --build

test:
	$(MANAGE) test
