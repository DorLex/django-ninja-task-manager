from datetime import datetime

from django.db.models import Q
from ninja import FilterSchema, Query

from tasks.enums import TaskStatus


class TaskFilter(FilterSchema):
    title: str | None = None

    status: TaskStatus | None = Query(
        default=None,
        description=f'Доступные статусы: {TaskStatus.values}',
    )

    created_at_start: datetime | None = Query(
        default=None,
        description=f'Пример: 2024-04-05 14:33:03',
    )

    created_at_finish: datetime | None = Query(
        default=None,
        description=f'Пример: 2024-04-05 15:09:16',
    )

    updated_at_start: datetime | None = Query(
        default=None,
        description=f'Пример: 2024-04-05 14:33:03',
    )

    updated_at_finish: datetime | None = Query(
        default=None,
        description=f'Пример: 2024-04-05 15:09:16',
    )

    def filter_title(self, value: str | None) -> Q:
        return Q(title__icontains=value) if value else Q()

    def filter_created_at_start(self, value: datetime | None) -> Q:
        return Q(created_at__gte=value) if value else Q()

    def filter_created_at_finish(self, value: datetime | None) -> Q:
        return Q(created_at__lte=value) if value else Q()

    def filter_updated_at_start(self, value: datetime | None) -> Q:
        return Q(updated_at__gte=value) if value else Q()

    def filter_updated_at_finish(self, value: datetime | None) -> Q:
        return Q(updated_at__lte=value) if value else Q()
