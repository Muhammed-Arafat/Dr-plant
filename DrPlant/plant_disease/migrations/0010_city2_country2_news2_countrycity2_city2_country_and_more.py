# Generated by Django 4.1.3 on 2023-06-28 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "plant_disease",
            "0009_city1_country1_news1_countrycity1_city1_country_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="City2",
            fields=[
                ("city_id", models.AutoField(primary_key=True, serialize=False)),
                ("city_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Country2",
            fields=[
                ("country_id", models.AutoField(primary_key=True, serialize=False)),
                ("country_name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="news2",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("img", models.ImageField(upload_to="photos")),
                ("time", models.DateField()),
                (
                    "case",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="plant_disease.diseases",
                    ),
                ),
                (
                    "city",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="plant_disease.city2",
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="plant_disease.country2",
                    ),
                ),
                (
                    "plant",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="plant_disease.plants",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CountryCity2",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="plant_disease.city2",
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="plant_disease.country2",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="city2",
            name="country",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="plant_disease.country2"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="city2", unique_together={("city_name", "country")},
        ),
    ]
