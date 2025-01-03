from django.http import HttpResponse
from django.shortcuts import render, redirect

# from .forms import PropertyForm, PropertyImageForm
from .serializers import PropertySerializer, ForListPropertyDeserializer, EntityPropertyDeserializer
from .models import Property, PropertyImage


def create_property(request):
    if request.method == 'POST':
        property_form = PropertySerializer(data=request.POST.dict())
        if property_form.is_valid():
            property_obj = property_form.save()
            return HttpResponse(status=201, content=str(dict(message='success', property=property_obj.id)))
        else:
            return HttpResponse(status=400, content=str(dict(message='error', errors=property_form.errors)))
    else:
        return render(request, 'base_property_form.html')


def get_property(request, pk):
    if request.method == 'GET':
        try:
            property_obj = Property.objects.get(pk=pk)
            property_deserializer = EntityPropertyDeserializer(property_obj)
            return render(request, 'property_info.html', {'property': property_deserializer.data})
        except Property.DoesNotExist:
            return HttpResponse(status=404, content=str(dict(message='error', errors='Property not found')))
    else:
        return HttpResponse(status=405, content=str(dict(message='error', errors='Method not allowed')))


def get_properties(request):
    if request.method == 'GET':
        properties = Property.objects.all()
        properties_list = []
        for property in properties:
            property_serializer = ForListPropertyDeserializer(property)
            if property_serializer.data:
                properties_list.append(property_serializer.data)
        return HttpResponse(status=200, content=str(dict(message='success', properties=properties_list)))
    else:
        return HttpResponse(status=405, content=str(dict(message='error', errors='Method not allowed')))