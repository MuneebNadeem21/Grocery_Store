from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _


# User Model
class User(AbstractUser):
    """
    Extends Django's AbstractUser with geolocation.
    """
    location = models.PointField(geography=True, null=True, blank=True)  # Stores latitude/longitude
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Store Model
class Store(models.Model):
    """
    Represents a store with geolocation.
    """
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, null=True, blank=True)
    location = models.PointField(geography=True)  # Geolocation for stores
    api_endpoint = models.URLField(max_length=500, null=True, blank=True)  # Optional: API endpoint for store data
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Category Model
class Category(models.Model):
    """
    Represents a product category.
    """
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


# Product Model
class Product(models.Model):
    """
    Represents a product.
    """
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField(null=True, blank=True)  # Optional: Product description
    image_url = models.URLField(max_length=500, null=True, blank=True)  # Optional: Image URL
    created_at = models.DateTimeField(auto_now_add=True)


# StoreProduct Model
class StoreProduct(models.Model):
    """
    Represents a product available in a store with price and stock info.
    """
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='store_products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(null=True, blank=True)  # Optional: Stock availability
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


# Deal Model
class Deal(models.Model):
    """
    Represents a deal or promotion for a product in a store.
    """
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='deals')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='deals')
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)
    promo_code = models.CharField(max_length=50, null=True, blank=True)  # Optional: Promo code
    buy_x = models.IntegerField(default=0)  # e.g., Buy 1
    get_y = models.IntegerField(default=0)  # e.g., Get 1
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)


# ShoppingList Model
class ShoppingList(models.Model):
    """
    Represents a user's shopping list.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shopping_lists')
    name = models.CharField(max_length=100)
    is_recurring = models.BooleanField(default=False)  # Indicates if the list is recurring
    recurrence_frequency = models.CharField(max_length=50, null=True, blank=True)  # e.g., "Weekly", "Monthly"
    next_recurrence_date = models.DateTimeField(null=True, blank=True)  # For scheduling recurring lists
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# ShoppingListItem Model
class ShoppingListItem(models.Model):
    """
    Represents an item in a shopping list.
    """
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='shopping_list_items')
    quantity = models.IntegerField(default=1)  # Quantity of the product
    created_at = models.DateTimeField(auto_now_add=True)


# UserNotification Model
class UserNotification(models.Model):
    """
    Represents notifications sent to users.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()  # Notification message
    is_read = models.BooleanField(default=False)  # Indicates if the notification has been read
    created_at = models.DateTimeField(auto_now_add=True)
