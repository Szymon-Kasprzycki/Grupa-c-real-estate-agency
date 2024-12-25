from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request, 'home.html') # we will create this file 

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/home/')
    
    # Render the login page template (GET request)
    return render(request, 'login.html')

def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        
        user = User.objects.filter(username=username)
        
        if user.exists():
            messages.info(request, "Username already in use.")
            return redirect('/register/')
        
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        
        user.set_password(password)
        user.save()

        messages.info(request, "Account created Successfully.")
        return redirect('/register/')
    
    return render(request, 'register.html')