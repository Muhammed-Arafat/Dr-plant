from django import forms
from plant_disease.models import *

class CityForm(forms.ModelForm):
    class Meta:
        model = CountryCity4
        fields = ['country','city']


class PlantsForm(forms.ModelForm):
    class Meta:
        model = Plants4
        fields = ['plants_name']
