from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from .forms import CustomerRegisterForm, CustomerUpdateInfoForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Customer


def home(request):
    return render(request, 'home.html')


def login_page(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
        return redirect(to='home_page')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect(to='login_page')
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect(to='login_page')
        else:
            login(request, user)
            return redirect(to='home_page')
    
    return render(request, 'login.html')


def register_page(request):
    if request.method == 'POST':
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.filter(username=username)
            if user.exists():
                messages.info(request, "Username already in use.")
                return redirect(to='register_page')

            user = User.objects.create_user(username=username, password=password)
            user.save()

            customer = form.save(commit=False)
            
            customer.user = user
            customer.save()
            
            messages.info(request, "Account created Successfully.")
            return redirect(to='home_page')
    else:
        form = CustomerRegisterForm()
    
    return render(request, 'register.html', {'form': form})


@login_required
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect(to='login_page')


@login_required
def customer_info(request):
    if request.user.is_authenticated:
        customer = Customer.objects.get(user=request.user)
        customer_personal_info = {
            'username': request.user.username,
            'first_name': customer.first_name,
            'last_name': customer.last_name,
            'gender': customer.gender,
            'email': customer.email,
            'phone_number': customer.phone_number,
            'address': customer.address,
            'preferences': customer.preferences,
            'created_at': customer.created_at,
            'updated_at': customer.updated_at
        }
        context = {
            'customer_personal_info': customer_personal_info
        }
        return render(request, 'customer_info.html', context)
    else:

        return render(request, 'login.html')


@login_required
def update_customer_info(request):
    if request.method == 'POST':
        form = CustomerUpdateInfoForm(request.POST)
        if form.is_valid():
            customer = Customer.objects.get(user=request.user)
            for field, value in form.cleaned_data.items():
                print(field, value)
                if value:
                    setattr(customer, field, value)
            customer.save()
            messages.info(request, "Account updated successfully.")
            return redirect(to='customer_info')
    else:
        form = CustomerUpdateInfoForm()
    return render(request, 'update_customer_info.html', {'form': form})
