from django.forms import ModelForm, TextInput
from django import forms
#from .models import Keyword

#creates a basic form for user input
class ProductForm(forms.Form):
    post = forms.CharField()
