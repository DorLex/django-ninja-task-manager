from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from tasks.views import router as tasks_router

api = NinjaAPI()

api.add_router('tasks/', tasks_router, tags=['tasks'])

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
