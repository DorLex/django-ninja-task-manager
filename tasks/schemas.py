from ninja import ModelSchema

from tasks.models import Task
from users.schemas import UserOutSchema


class TaskSchema(ModelSchema):
    class Meta:
        model = Task
        fields = '__all__'


class TaskWithOwnerSchema(TaskSchema):
    user: UserOutSchema
