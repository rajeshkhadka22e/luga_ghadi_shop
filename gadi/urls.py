# myapp/urls.py

from django.urls import path
from .views import home_view

urlpatterns = [
    path('', home_view, name='home'),  # This will serve the home view at the root URL
]
