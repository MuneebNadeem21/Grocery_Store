from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StoreViewSet, ProductViewSet, ShoppingListViewSet

router = DefaultRouter()
router.register('stores', StoreViewSet)
router.register('products', ProductViewSet)
router.register('shopping-lists', ShoppingListViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
