from ninja import ModelSchema

from tasks.models import Task
from users.schemas import UserOutSchema


class TaskSchema(ModelSchema):
    class Meta:
        model = Task
        fields = '__all__'


class TaskCreateSchema(ModelSchema):
    class Meta:
        model = Task
        fields = (
            'title',
            'description',
        )


class TaskUpdateSchema(ModelSchema):
    class Meta:
        model = Task
        fields = (
            'title',
            'description',
            'status',
        )


class TaskWithOwnerSchema(TaskSchema):
    user: UserOutSchema
