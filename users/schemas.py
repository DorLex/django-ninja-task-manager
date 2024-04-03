from django.contrib.auth import get_user_model
from ninja import ModelSchema

User = get_user_model()


class UserOutSchema(ModelSchema):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
        )
