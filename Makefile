MANAGE = python manage.py

migrate:
	$(MANAGE) makemigrations
	$(MANAGE) migrate

superuser:
	$(MANAGE) createsuperuser

run:
	uvicorn core.asgi:application --reload

celery_run:
	celery -A celery_layer.celery_app:app worker -l INFO

flower_run:
	celery -A celery_layer.celery_app:app flower --conf='./celery_layer/flower_config.py'

docker_run:
	docker compose up --build

test:
	$(MANAGE) test
