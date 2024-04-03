from django.core.handlers.asgi import ASGIRequest
from ninja import Router

from tasks.models import Task
from tasks.repository import TaskRepository
from tasks.schemas import TaskSchema

router = Router()

task_repository = TaskRepository()


@router.get('/', response=list[TaskSchema])
async def list_tasks(request: ASGIRequest):
    tasks: list[Task] = await task_repository.list()
    return tasks


@router.get('/{task_id}', response=TaskSchema)
async def get_task(request: ASGIRequest, task_id: int):
    task: Task = await task_repository.get(task_id)
    return task
