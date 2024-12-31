from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from .forms import CustomerRegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/customers/login/')
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/customers/login/')
        else:
            login(request, user)
            return redirect('/customers/home/')
    
    return render(request, 'login.html')

def register_page(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        form = CustomerRegisterForm(request.POST)
        if form.is_valid():

            user = User.objects.filter(username=username)
            if user.exists():
                messages.info(request, "Username already in use.")
                return redirect('/customers/register/')

            user = User.objects.create_user(username=username)
            user.set_password(password)
            user.save()

            customer = form.save(commit=False)
            
            customer.user = user
            customer.save()
            
            messages.info(request, "Account created Successfully.")
            return redirect('/customers/home/')
    else:
        form = CustomerRegisterForm()
    
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request, 'login.html')

@login_required(login_url='/customers/login/')
def customer_info(request):
    return render(request, 'customer_info.html')

