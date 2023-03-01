from django import forms
from .models import my_movie

class movieform(forms.ModelForm):
    class Meta:
        model = my_movie
        fields = ['name','about','year','img']