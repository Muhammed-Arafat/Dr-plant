# Generated by Django 4.1.3 on 2023-06-27 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("plant_disease", "0005_alter_diseases_plant"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="plant",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="plant_disease.plants",
            ),
        ),
    ]
