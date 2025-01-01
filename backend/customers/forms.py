from django import forms
from django.forms import ModelForm
from .models import Customer

class CustomerRegisterForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'gender', 'email', 'phone_number', 'address']

class CustomerUpdateInfoForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'gender', 'email', 'phone_number', 'address', 'preferences']
    
    def __init__(self, *args, **kwargs):
        super(CustomerUpdateInfoForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False