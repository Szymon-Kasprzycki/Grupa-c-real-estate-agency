from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


class Property(models.Model):
    class TYPES(models.TextChoices):
        HOUSE = 'House'
        FLAT = 'Flat'
        APARTMENT = 'Apartment'
        STUDIO = 'Studio'
    owner = models.JSONField()
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    type = models.CharField(choices=TYPES, max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveIntegerField(blank=True, null=True)
    bathrooms = models.PositiveIntegerField(blank=True, null=True)
    garage = models.PositiveIntegerField(blank=True, null=True)
    sqft = models.PositiveIntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    photo_main = models.URLField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('property', kwargs={'pk': self.pk})

    def get_contact_info(self):
        return f"{self.owner['first_name']} {self.owner['last_name']} - {self.owner['email']}"

    def get_phone_number(self):
        return self.owner['phone']

    def get_address(self):
        return f"{self.city}, {self.country}"

    class Meta:
        ordering = ['price']


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    photo = models.URLField()

    def __str__(self):
        return self.property.name

    class Meta:
        verbose_name = 'Property Image'
        verbose_name_plural = 'Property Images'