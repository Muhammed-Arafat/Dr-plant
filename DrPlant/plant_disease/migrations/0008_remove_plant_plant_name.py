# Generated by Django 4.1.3 on 2023-06-27 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("plant_disease", "0007_plant_plants_name"),
    ]

    operations = [
        migrations.RemoveField(model_name="plant", name="plant_name",),
    ]