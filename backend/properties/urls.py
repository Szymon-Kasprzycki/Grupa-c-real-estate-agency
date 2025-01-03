from django.urls import path
from . import views, endpoints

urlpatterns = [
    path('create', endpoints.create_property, name='create_property'),
    path('get/<int:pk>', endpoints.get_property, name='get_property'),
    path('get', endpoints.get_properties, name='get_properties'),
]