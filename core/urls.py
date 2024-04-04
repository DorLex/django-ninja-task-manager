from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController

from tasks.views import router as tasks_router

api = NinjaExtraAPI()

api.register_controllers(NinjaJWTDefaultController)

api.add_router('tasks/', tasks_router, tags=['tasks'])

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
