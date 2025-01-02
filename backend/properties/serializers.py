from rest_framework import serializers
from .models import Property, PropertyImage

from decimal import Decimal
import json


class PropertySerializer(serializers.ModelSerializer):
    owner_first_name = serializers.CharField(max_length=100)
    owner_last_name = serializers.CharField(max_length=100)
    owner_email = serializers.EmailField()
    owner_phone = serializers.CharField(max_length=100)

    class Meta:
        model = Property
        fields = ['name', 'description', 'type', 'city', 'country', 'price', 'bedrooms', 'bathrooms', 'garage', 'sqft',
                  'lot_size', 'photo_main', 'owner_first_name', 'owner_last_name', 'owner_email', 'owner_phone']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.is_valid():
            self.validate(self.validated_data)

    def to_internal_value(self, data):
        data = data.copy()

        owner = {
            'first_name': data.pop('owner_first_name'),
            'last_name': data.pop('owner_last_name'),
            'email': data.pop('owner_email'),
            'phone': data.pop('owner_phone')
        }
        data['owner'] = owner

        # Convert price to Decimal
        if 'price' in data:
            try:
                data['price'] = Decimal(data.get('price'))
            except (TypeError, ValueError):
                raise serializers.ValidationError({"price": "Value must be a decimal number."})

        # Convert other fields to appropriate types
        if 'sqft' in data:
            data['sqft'] = int(data.get('sqft'))
        if 'garage' in data:
            data['garage'] = int(data.get('garage'))
        if 'bedrooms' in data:
            data['bedrooms'] = int(data.get('bedrooms'))
        if 'bathrooms' in data:
            data['bathrooms'] = int(data.get('bathrooms'))
        if 'lot_size' in data:
            try:
                data['lot_size'] = Decimal(data.get('lot_size'))
            except (TypeError, ValueError):
                raise serializers.ValidationError({"lot_size": "Value must be a decimal number."})

        return data

    def validate(self, data):
        if data['type'] and data["type"] not in Property.TYPES:
            raise serializers.ValidationError("Invalid property type")

        if data['price'] < 0:
            raise serializers.ValidationError("Price must be a positive number")

        if data['sqft'] < 0:
            raise serializers.ValidationError("Square footage must be a positive number")

        if 'lot_size' in data and data['lot_size'] < 0:
            raise serializers.ValidationError("Lot size must be a positive number")

        if 'bedrooms' in data and data['bedrooms'] < 0:
            raise serializers.ValidationError("Number of bedrooms must be a positive number")

        if 'bathrooms' in data and data['bathrooms'] < 0:
            raise serializers.ValidationError("Number of bathrooms must be a positive number")

        if 'garage' in data and data['garage'] < 0:
            raise serializers.ValidationError("Number of garages must be a positive number")

        if 'owner_phone' in data and not data['owner_phone'].isdigit():
            raise serializers.ValidationError("Phone number must contain only numbers")

        return data

    def create(self, validated_data):
        validated_data['owner'] = json.dumps(validated_data['owner'])
        photo_main = validated_data.pop('photo')
        if photo_main:
            validated_data['photo_main'] = photo_main

        validated_data.pop('csrfmiddlewaretoken', None)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        owner = {
            'first_name': validated_data.get('owner_first_name', instance.owner['first_name']),
            'last_name': validated_data.get('owner_last_name', instance.owner['last_name']),
            'email': validated_data.get('owner_email', instance.owner['email']),
            'phone': validated_data.get('owner_phone', instance.owner['phone'])
        }
        instance.owner = json.dumps(owner)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.type = validated_data.get('type', instance.type)
        instance.city = validated_data.get('city', instance.city)
        instance.country = validated_data.get('country', instance.country)
        instance.price = validated_data.get('price', instance.price)
        instance.bedrooms = validated_data.get('bedrooms', instance.bedrooms)
        instance.bathrooms = validated_data.get('bathrooms', instance.bathrooms)
        instance.garage = validated_data.get('garage', instance.garage)
        instance.sqft = validated_data.get('sqft', instance.sqft)
        instance.lot_size = validated_data.get('lot_size', instance.lot_size)
        instance.photo_main = validated_data.get('photo_main', instance.photo_main)
        instance.save()
        return instance


class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.is_valid():
            self.validate(self.data)

    def create(self, validated_data):
        return PropertyImage.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.photo = validated_data.get('photo', instance.photo)
        instance.save()
        return instance