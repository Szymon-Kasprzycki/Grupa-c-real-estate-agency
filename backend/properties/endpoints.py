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
            # return 201 created status
            return HttpResponse(status=201)
    else:
        return render(request, '404.html')
