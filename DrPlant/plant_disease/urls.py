from django.urls import path
from . import views


urlpatterns = [
    path("plant_disease", views.plant_disease_def, name="plant_disease"),

]
