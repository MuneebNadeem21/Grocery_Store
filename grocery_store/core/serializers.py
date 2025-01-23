from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from .models import User, Store, Product, Deal, ShoppingList, ShoppingListItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'location']

class StoreSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Store
        geo_field = 'location'
        fields = ['id', 'name', 'address', 'location']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'description', 'image_url']

class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingList
        fields = ['id', 'user', 'name', 'is_recurring', 'recurrence_frequency', 'next_recurrence_date']
