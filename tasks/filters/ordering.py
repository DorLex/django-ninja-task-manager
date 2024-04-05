from enum import Enum

from django.db.models import QuerySet
from ninja import Schema, Query


class TaskOrderingEnum(Enum):
    id = 'id'
    _id = '-id'
    title = 'title'
    _title = '-title'
    status = 'status'
    _status = '-status'

    @classmethod
    def values(cls):
        return [enum_field.value for enum_field in cls]


class TaskOrdering(Schema):
    order_by_field: TaskOrderingEnum | None = Query(
        default=None,
        description=f'Доступные поля: {TaskOrderingEnum.values()}',
    )

    def order(self, qs: QuerySet) -> QuerySet:
        if self.order_by_field:
            qs = qs.order_by(self.order_by_field.value)

        return qs
