from django.urls import path, include
from rest_framework import routers
from rest_api.views import StoreViewSet

router = routers.SimpleRouter()
router.register('', StoreViewSet, basename='stores')