

from django.contrib.auth.models import User
from .models import Appoinment
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' ,'email' , 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-group'})

class AppoinmentForm(ModelForm):
    class Meta:
        model = Appoinment
        fields = ['department', 'name', 'email', 'date', 'phone', 'message']
        widgets = {
        'date': forms.DateInput(format=('%m/%d/%Y'), attrs={'type':'date'}),
    }

    def __init__(self, *args, **kwargs):
        super(AppoinmentForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':"form-control"})    