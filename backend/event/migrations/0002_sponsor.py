# Generated by Django 2.2.14 on 2020-07-21 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sponsor",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(max_length=256)),
                ("logo_image", models.SlugField(max_length=150)),
                ("sponsor_level", models.TextField()),
                ("presenter", models.BooleanField()),
                ("website", models.URLField()),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sponsor_location",
                        to="event.Location",
                    ),
                ),
            ],
        ),
    ]
