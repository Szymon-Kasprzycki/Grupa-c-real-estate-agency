from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    class Genders(models.TextChoices):
        Male = 'Male'
        Female = 'Female'
        Other = 'Other'

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100 , blank=True)
    gender = models.CharField(max_length=10, choices=Genders, default=Genders.Other)
    email = models.EmailField()
    phone_number = models.CharField(max_length=9, blank=True) # we assume that the phone number is 9 digits (like in Poland)
    address = models.CharField(max_length=1000, blank=True)
    preferences = models.JSONField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
