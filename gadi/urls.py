from django.urls import path,include
from .views import (
    home_view,
    boys_product,
    checkout_cart_view,
    register_account_view,
    login_account_view,
    buy_now_views,
    category_products,  # Add the dynamic category handler
)

urlpatterns = [
    path('', home_view, name='home'),  
    path('<int:id>/', home_view, name='product_detail'),
    path('boys_product/', boys_product, name='boys_product'),  # Optional, replace with category_products if needed
    path('cart/<int:product_id>/', checkout_cart_view, name='cart'),
    path('register_account/', register_account_view, name='register_account'),
    path('login_account/', login_account_view, name='login_account'),
    path('buy_now/<int:product_id>/', buy_now_views, name='buy_now'),

    # Dynamic category-based URL
    path('products/<str:category_name>/', category_products, name='category_products'),
    
]
