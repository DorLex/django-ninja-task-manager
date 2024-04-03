from django.shortcuts import aget_object_or_404, aget_list_or_404

from tasks.models import Task


class TaskRepository:
    _model = Task

    async def get(self, task_id: int, user_id: int) -> Task:
        task = await aget_object_or_404(self._model, pk=task_id, user_id=user_id)
        return task

    async def list(self, user_id: int) -> list[Task]:
        qs = self._model.objects.filter(user_id=user_id)
        tasks = await aget_list_or_404(qs)
        return tasks
