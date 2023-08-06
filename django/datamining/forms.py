
from django import forms
from .models import TableForForm
from django.forms import ModelForm, TextInput

class TableForFormForm(ModelForm):
    class Meta:
        model = TableForForm
        fields = ['name', 'hero_name']
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название Предмета',
            }),
            "hero_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя Героя',
            }),
        }











