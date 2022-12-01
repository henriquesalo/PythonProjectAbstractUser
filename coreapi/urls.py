from django.contrib import admin
#include = importando as rotas / path = endpoint
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user.views import UserViewSet

router = DefaultRouter()
router.register('user',UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]