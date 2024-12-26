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
            property_type = property_obj.type.lower()
            template_name = f'{property_type}_template.html'
            return render(request, template_name, {'property': property_obj})
        else:
            return HttpResponse(status=400, content=dict(message='error', errors=[*property_form.errors, *image_form.errors]))
    else:
        property_form = PropertyForm()
        image_form = PropertyImageForm()
        return render(request, 'base_property_form.html', {
            'property_form': property_form,
            'image_form': image_form
        })