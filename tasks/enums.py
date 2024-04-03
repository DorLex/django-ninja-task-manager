from django.db import models


class TaskStatus(models.TextChoices):
    created = 'created'
    active = 'active'
    completed = 'completed'
