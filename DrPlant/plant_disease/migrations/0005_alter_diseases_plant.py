# Generated by Django 4.1.3 on 2023-06-27 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("plant_disease", "0004_plants"),
    ]

    operations = [
        migrations.AlterField(
            model_name="diseases",
            name="plant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="plant_disease.plants"
            ),
        ),
    ]
