from asgiref.sync import sync_to_async
from django.core.exceptions import ValidationError
from django.shortcuts import aget_object_or_404, aget_list_or_404
from ninja_extra import status
from ninja_extra.exceptions import APIException

from tasks.models import Task
from tasks.schemas import TaskCreateSchema, TaskUpdateSchema


class TaskRepository:
    _model = Task

    async def get(self, task_id: int, user_id: int) -> Task:
        task = await aget_object_or_404(self._model, pk=task_id, user_id=user_id)
        return task

    async def list(self, user_id: int) -> list[Task]:
        qs = self._model.objects.filter(user_id=user_id)
        tasks = await aget_list_or_404(qs)
        return tasks

    async def create(self, task_data: TaskCreateSchema, user_id: int) -> Task:
        task = await self._model.objects.acreate(**task_data.dict(), user_id=user_id)
        return task

    async def update(self, task_id: int, task_data: TaskUpdateSchema, user_id: int):
        task = await aget_object_or_404(self._model, pk=task_id, user_id=user_id)
        for attr, value in task_data.dict().items():
            setattr(task, attr, value)

        try:
            await sync_to_async(task.full_clean)()
            await task.asave()
            return task

        except ValidationError as ex:
            raise APIException(
                detail=ex.error_dict,
                code=status.HTTP_400_BAD_REQUEST
            )
