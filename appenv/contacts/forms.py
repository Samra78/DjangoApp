from django import forms
from django.forms.models import ModelFormMetaclass
from .models import Contact

class SaveContact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','address','phone','email','contact_type']