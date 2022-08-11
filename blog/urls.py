from django.urls import path, include
from .views import *

from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'categories', BlogCategoryViewSet)
router.register(r'posts', BlogPostByCategoryViewSet, basename='posts')
router.register(r'post', BlogPostBySlugViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path("posts/", BlogPostViewSet.as_view({'get', 'list'}))
]
