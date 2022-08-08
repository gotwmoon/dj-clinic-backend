
from django.contrib.auth.models import User
from .models import Appoinment, Patient
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from captcha.fields import CaptchaField


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' ,'email' , 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-group'})

class AppoinmentForm(ModelForm):
    captcha = CaptchaField()
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

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'email', 'username', 'birthday', 'phone', 'gender']        
        widgets = {
        'birthday': forms.DateInput(format=('%m/%d/%Y'), attrs={'type':'date'}),
    } 

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':"form-control"})    