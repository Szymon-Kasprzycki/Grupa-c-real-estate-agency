from django.http import HttpResponse
from django.shortcuts import render, redirect

# from .forms import PropertyForm, PropertyImageForm
from .serializers import PropertySerializer, PropertyImageSerializer


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