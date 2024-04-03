from ninja import Router
from ninja_jwt.authentication import AsyncJWTAuth

from tasks.models import Task
from tasks.repository import TaskRepository
from tasks.schemas import TaskSchema

router = Router(auth=AsyncJWTAuth())

task_repository = TaskRepository()


@router.get('/', response=list[TaskSchema])
async def list_tasks(request):
    tasks: list[Task] = await task_repository.list(request.user.id)
    return tasks


@router.get('/{task_id}', response=TaskSchema)
async def get_task(request, task_id: int):
    task: Task = await task_repository.get(task_id, request.user.id)
    return task
