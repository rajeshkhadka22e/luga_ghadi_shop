# myapp/urls.py

from django.urls import path
from .views import home_view,boys_product,checkout_cart_view,register_account_view,login_account_view,buy_now_views

urlpatterns = [
    path('', home_view, name='home'),  # This will serve the home view at the root URL
    path('boys_product/', boys_product, name='boys_product'),
    path('cart/', checkout_cart_view, name='cart'),
    path('register_account/', register_account_view, name='register_account'),
    path('login_account/', login_account_view, name='login_account'),
    path('buy_now/', buy_now_views, name='buy_now'),




]

