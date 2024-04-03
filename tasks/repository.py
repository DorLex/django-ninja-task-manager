from django.shortcuts import aget_object_or_404, aget_list_or_404

from tasks.models import Task


class TaskRepository:
    _model = Task

    async def get(self, task_id: int) -> Task:
        qs = self._model.objects.all().select_related('user')
        task = await aget_object_or_404(qs, pk=task_id)
        return task

    async def list(self) -> list[Task]:
        qs = self._model.objects.all().select_related('user')
        tasks = await aget_list_or_404(qs)
        return tasks
