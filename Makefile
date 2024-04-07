MANAGE = python manage.py

migrate:
	$(MANAGE) makemigrations
	$(MANAGE) migrate

superuser:
	$(MANAGE) createsuperuser

run:
	uvicorn core.asgi:application --reload

celery_run:
	celery -A core worker -l INFO

docker_run:
	docker compose up --build
