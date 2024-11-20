# models.py

from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('unisex', 'Unisex'),
        ('boys', 'Boys'),
        ('ladies', 'Ladies'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    sizes = models.ManyToManyField('Size', blank=True)
    colors = models.ManyToManyField('Color', blank=True)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    main_image = models.ImageField(upload_to="products/", null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='unisex')

    def __str__(self):
        return self.name

class Size(models.Model):
    size_name = models.CharField(max_length=20, default= True)

    def __str__(self):
        return self.size_name

class Color(models.Model):
    color_name = models.CharField(max_length=20, default=True)

    def __str__(self):
        return self.color_name
class Cart(models.Model):
    name = models.CharField(max_length=255)  # Unique identifier for each cart
    products = models.ManyToManyField(Product, through='CartItem')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)







    




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=15, blank=False, null=False)  # Ensure phone is required

    def __str__(self):
        return f"{self.user.username} - {self.phone}"