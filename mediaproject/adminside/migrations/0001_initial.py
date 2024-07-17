# Generated by Django 5.0.3 on 2024-04-11 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BasicInfo",
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
                ("logo", models.ImageField(upload_to="logos/")),
                ("contact", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=255)),
                ("facebook_link", models.URLField(blank=True)),
                ("twitter_link", models.URLField(blank=True)),
                ("instagram_link", models.URLField(blank=True)),
                ("about_us", models.TextField(blank=True)),
                ("google_maps_link", models.URLField(blank=True)),
            ],
        ),
    ]
