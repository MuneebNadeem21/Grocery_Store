from rest_framework import viewsets
from .models import Store, Product, ShoppingList
from .serializers import StoreSerializer, ProductSerializer, ShoppingListSerializer

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    # testing file hai 
    serializer_class = StoreSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    print(queryset)
    serializer_class = ProductSerializer
    print(serializer_class)

class ShoppingListViewSet(viewsets.ModelViewSet):
    print('test')
    print('test2')
    print('feature3')
    print('feature 4')
    print('MN-23')
    print('test PR')
    print('again  push')

    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
