
from django import forms
from .models import TableForForm, ServisesInSupport
from django.forms import ModelForm, TextInput, DateInput

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

class ServisesInSupportForm(ModelForm):
    class Meta:
        model = ServisesInSupport
        fields = ['name', 'guid_server', 'appearance_time', 'discription', 'ip_adreses']
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название Сервиса',
            }),
            "guid_server": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'GUID Информационной системы',
            }),
            "appearance_time": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата принятия в поддержку Unix',
            }),
            "discription": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дополнительная информация',
            }),
            "ip_adreses": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сетевые адреса',
            }),
        }
