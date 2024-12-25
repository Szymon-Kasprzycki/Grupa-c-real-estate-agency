from django.urls import path
from .views import home, login_page, register_page

urlpatterns = [
    path('home/', home),
    path('login/', login_page),
    path('register/', register_page), 
]
