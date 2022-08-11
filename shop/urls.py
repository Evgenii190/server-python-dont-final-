from django.urls import path, include
from .views import *

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)
router.register(r'category', ProductItemsViewSet)
router.register(r'images', ProductSliderViewSet)
router.register(r'itemsCategories', ProductSubCategoryViewSet)
router.register(r'categories', ProductCategoryViewSet)
router.register(r'subcategory', ProductsSubCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('request', RequestMessageAPIView.as_view()),
    path('productsQuery', ProductsQueryAPIView.as_view())
]
