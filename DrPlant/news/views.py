
from django.shortcuts import render
from plant_disease.models import *
from django.http import JsonResponse
from plant_disease.forms import CityForm,PlantsForm
# Create your views here.
def news_def(request):
    if request.method == 'POST':
        print(request.POST['country'])
        print(request.POST['city'])
        print(request.POST['plant'])
        news=news4.objects.filter(plant=request.POST['plant'],city=request.POST['city'],country=request.POST['country'])
        countries = Country4.objects.all()
        cities = City4.objects.all()
        plants = Plants4.objects.all()
        context={
        'news':news,
        'countries': countries,
        'cities': cities,
        'plants': plants
        }
        return render(request, "news.html",context)
    else:

        context={
    #'diseases':Diseases.objects.all(),
    #'countries':Countries.objects.all(),
    #'cities':Cities.objects.all(),
        'news':news4.objects.all(),
        'countries': Country4.objects.all(),
        'cities': City4.objects.all(),
        'plants': Plants4.objects.all()
        }
        return render(request, "news.html",context)

# Create your views here.
