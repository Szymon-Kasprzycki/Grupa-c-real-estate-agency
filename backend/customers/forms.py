from django.forms import ModelForm


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'