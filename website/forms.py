from dataclasses import fields
from .models import Contact, Newsletter
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'        