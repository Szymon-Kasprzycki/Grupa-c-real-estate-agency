from django.urls import path
from . import views, endpoints

urlpatterns = [
    path('create', endpoints.create_property, name='create_property'),
]