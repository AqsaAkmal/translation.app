from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('', views.home, name='home'),  # Use the 'home' function
]

