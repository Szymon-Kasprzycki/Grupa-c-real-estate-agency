from django.urls import path, include
from .views import home, login_page, register_page, customer_info

urlpatterns = [
    path('home/', home, name='home_page'),
    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register_page'), 
    path('info/', customer_info, name='customer_info'), 

]
