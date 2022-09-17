from django.urls import path, include
from . import views

urlpatterns = [
    # home
    path('', views.home, name='home'),
    path('', include("django.contrib.auth.urls")),
]
