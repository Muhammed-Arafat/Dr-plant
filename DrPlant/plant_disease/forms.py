from django import forms
from .models import *
from datetime import date

class DatePickerInput(forms.DateInput):
        input_type = 'date'

class CityForm(forms.ModelForm):
    class Meta:
        model = CountryCity4
        fields = ['country','city']

class PlantsForm(forms.ModelForm):
    class Meta:
        model = Plants4
        fields = ['plants_name']

class ImagesForm(forms.ModelForm):
    class Meta:
        model=news
        fields=['time']
        widgets={
        'time': DatePickerInput(attrs={'value': date.today(),'class':'ttt'}),
        }
