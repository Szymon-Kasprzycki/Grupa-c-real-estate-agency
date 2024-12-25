from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from .models import Customer


def home(request):
    return render(request, 'home.html')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('login/')
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('login/')
        else:
            login(request, user)
            return redirect('home/')
    
    return render(request, 'login.html')

def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        
        user = User.objects.filter(username=username)
        
        if user.exists():
            messages.info(request, "Username already in use.")
            return redirect('register/')
        
        user = User.objects.create_user(username=username)
        user.set_password(password)
        user.save()

        customer = Customer.objects.create(
            user=user, 
            first_name=first_name, 
            last_name=last_name, 
            email=email,
            phone_number=phone_number
            )

        messages.info(request, "Account created Successfully.")
        return redirect('register/')
    
    return render(request, 'register.html')