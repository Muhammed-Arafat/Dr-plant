# Generated by Django 4.1.3 on 2023-06-27 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("plant_disease", "0006_news_plant"),
    ]

    operations = [
        migrations.AddField(
            model_name="plant",
            name="plants_name",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="plant_disease.plants",
            ),
            preserve_default=False,
        ),
    ]
