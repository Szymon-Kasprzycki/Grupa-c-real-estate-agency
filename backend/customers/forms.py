from django.forms import ModelForm
from .models import Customer

class CustomerRegisterForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'gender', 'email', 'phone_number', 'address']
