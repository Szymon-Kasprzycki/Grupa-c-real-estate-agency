from django.forms import ModelForm
from .models import Property, PropertyImage


class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = '__all__'


class PropertyImageForm(ModelForm):
    class Meta:
        model = PropertyImage
        fields = '__all__'