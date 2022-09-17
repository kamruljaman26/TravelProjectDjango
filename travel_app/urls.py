from django.urls import path, include
from . import views

urlpatterns = [
    # home
    path('', views.home, name='home'),
    path('register', views.registration, name='register'),
    path('', include("django.contrib.auth.urls")),
]
