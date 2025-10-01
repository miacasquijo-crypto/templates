# pages/urls.py

from django.urls import path
from .views import home_view, about_view

urlpatterns = [
    # URL for /
    path('', home_view, name='home'),
    # URL for /about/
    path('about/', about_view, name='about'),
]