from ninja import Router, Query
from ninja_jwt.authentication import AsyncJWTAuth

from tasks.filters.filter import TaskFilter
from tasks.filters.ordering import TaskOrdering
from tasks.models import Task
from tasks.repository import TaskRepository
from tasks.schemas import TaskOutSchema, TaskCreateSchema, TaskUpdateSchema

router = Router(auth=AsyncJWTAuth())

task_repository = TaskRepository()


@router.get('/', response=list[TaskOutSchema])
async def list_tasks(request, filters: TaskFilter = Query(), ordering: TaskOrdering = Query()):
    tasks: list[Task] = await task_repository.list(request.user.id, filters, ordering)
    return tasks


@router.get('/{task_id}', response=TaskOutSchema)
async def get_task(request, task_id: int):
    task: Task = await task_repository.get(task_id, request.user.id)
    return task


@router.post('/', response=TaskOutSchema)
async def create_task(request, task_data: TaskCreateSchema):
    task: Task = await task_repository.create(task_data, request.user.id)
    return task


@router.put('/{task_id}', response=TaskOutSchema)
async def update_task(request, task_id: int, task_data: TaskUpdateSchema):
    task: Task = await task_repository.update(task_id, task_data, request.user.id)
    return task


@router.delete('/{task_id}', response=TaskOutSchema)
async def delete_task(request, task_id: int):
    task: Task = await task_repository.delete(task_id, request.user.id)
    return task
