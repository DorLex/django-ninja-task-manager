from ninja import ModelSchema

from tasks.models import Task
from users.schemas import UserOutSchema


class TaskSchema(ModelSchema):
    user: UserOutSchema

    class Meta:
        model = Task
        fields = '__all__'
