from django.shortcuts import aget_object_or_404, aget_list_or_404

from tasks.filters.filter import TaskFilter
from tasks.filters.ordering import TaskOrdering
from tasks.models import Task
from tasks.schemas import TaskCreateSchema, TaskUpdateSchema


class TaskRepository:
    _model = Task

    async def get(self, task_id: int, user_id: int) -> Task:
        task = await aget_object_or_404(self._model, pk=task_id, user_id=user_id)
        return task

    async def list(self, user_id: int, filters: TaskFilter, ordering: TaskOrdering) -> list[Task]:
        qs = self._model.objects.filter(user_id=user_id)
        qs = filters.filter(qs)
        qs = ordering.order(qs)

        tasks = await aget_list_or_404(qs)

        return tasks

    async def create(self, task_data: TaskCreateSchema, user_id: int) -> Task:
        task = await self._model.objects.acreate(**task_data.dict(), user_id=user_id)
        return task

    async def update(self, task_id: int, task_data: TaskUpdateSchema, user_id: int):
        task = await aget_object_or_404(self._model, pk=task_id, user_id=user_id)
        for attr, value in task_data.dict().items():
            setattr(task, attr, value)

        await task.asave()
        return task

    async def delete(self, task_id: int, user_id: int):
        task = await aget_object_or_404(self._model, pk=task_id, user_id=user_id)
        await task.adelete()
        return task
