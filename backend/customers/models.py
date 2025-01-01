from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator


class Customer(models.Model):
    class Genders(models.TextChoices):
        Male = 'Male'
        Female = 'Female'
        Other = 'Other'

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100 , blank=True)
    gender = models.CharField(max_length=10, choices=Genders, default=Genders.Other)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=9,
                                    validators=[MinLengthValidator(9), 
                                                MaxLengthValidator(9),
                                                RegexValidator(regex=r'^\d{9}$', message='Phone number must be 9 digits long and contain only numbers.')],
                                    blank=True,
                                    unique=True)
    address = models.CharField(max_length=1000, blank=True)
    preferences = models.JSONField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_gender(self):
        return self.gender
    
    def get_email(self):
        return self.email
    
    def get_phone_number(self):
        return self.phone_number
    
    def get_address(self):
        return self.address
    
    def get_preferences(self):
        return self.preferences
    
    def get_created_at(self):
        return self.created_at
    
    def get_updated_at(self):
        return self.updated_at
    