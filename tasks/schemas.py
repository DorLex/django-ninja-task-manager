from ninja import ModelSchema

from tasks.enums import TaskStatus
from tasks.models import Task
from users.schemas import UserOutSchema


class TaskOutSchema(ModelSchema):
    class Meta:
        model = Task
        fields = '__all__'


class TaskCreateSchema(ModelSchema):
    status: TaskStatus = TaskStatus.created

    class Meta:
        model = Task
        fields = (
            'title',
            'description',
            'status',
        )


class TaskUpdateSchema(ModelSchema):
    status: TaskStatus

    class Meta:
        model = Task
        fields = (
            'title',
            'description',
            'status',
        )


class TaskWithOwnerSchema(TaskOutSchema):
    user: UserOutSchema
