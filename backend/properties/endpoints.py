from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import PropertyForm, PropertyImageForm


def create_property(request):
    if request.method == 'POST':
        property_form = PropertyForm(request.POST)
        image_form = PropertyImageForm(request.POST, request.FILES)
        if property_form.is_valid() and image_form.is_valid():
            property_obj = property_form.save()
            image = image_form.save(commit=False)
            image.property = property_obj
            image.save()
            return HttpResponse(status=201, content=dict(message='success', property=property_obj.id, image=image.id))
        else:
            return HttpResponse(status=400, content=dict(message='error', errors=[*property_form.errors, *image_form.errors]))
    else:
        return render(request, '404.html')
