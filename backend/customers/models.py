from django.db import models
from django.contrib.auth.hashers import make_password


class Customer(models.Model):
    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        OTHER = 'O', 'Other'

    customerID = models.CharField(max_length=100, primary_key=True) # login
    password = models.CharField(max_length=100)

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.OTHER)
    email = models.EmailField()
    phone = models.CharField(max_length=9) # we assume that the phone number is 9 digits (like in Poland)
    address = models.CharField(max_length=1000)
    preferences = models.JSONField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.pk or 'password' in self.get_dirty_fields():
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
