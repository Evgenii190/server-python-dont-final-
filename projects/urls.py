from django.urls import path, include
from .views import *

from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'categories', ProjectCategoryViewSet)
router.register(r'project', ProjectViewSet)
router.register(r'characteristics', ProjectCharacteristicViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
