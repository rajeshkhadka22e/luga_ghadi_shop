# admin.py

from django.contrib import admin
from .models import Product, Size, Color,Cart, CartItem,UserProfile

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'selling_price', 'discounted_price', 'category')
    search_fields = ('name', 'category')
    list_filter = ('category',)

class SizeAdmin(admin.ModelAdmin):
    list_display = ('size_name',)
    search_fields = ('size_name',)

class ColorAdmin(admin.ModelAdmin):
    list_display = ('color_name',)
    search_fields = ('color_name',)
# @admin.register(Cart)
# class CartAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     search_fields = ('name',)
#     filter_horizontal = ('products',)  # If using ManyToManyField directly

# Register the CartItem model
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')
    list_filter = ('cart', 'product')
# Register the models
admin.site.register(Product, ProductAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Color, ColorAdmin)



@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')