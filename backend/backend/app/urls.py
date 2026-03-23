"""Backend application URL configuration."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import BulletinViewSet


router = DefaultRouter()
router.register(r'bulletins', BulletinViewSet, basename='bulletin')

urlpatterns = [
    path('', include(router.urls)),
]
