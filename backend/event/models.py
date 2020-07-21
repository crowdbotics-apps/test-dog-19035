from django.conf import settings
from django.db import models


class FAQ(models.Model):
    "Generated Model"
    title = models.CharField(max_length=256,)
    description = models.TextField()


class Schedule(models.Model):
    "Generated Model"
    date_time = models.DateTimeField()
    description = models.TextField()
    location = models.ForeignKey(
        "event.Location", on_delete=models.CASCADE, related_name="schedule_location",
    )
    track = models.TextField()


class Presenter(models.Model):
    "Generated Model"
    name = models.CharField(max_length=256,)
    title = models.CharField(max_length=256,)
    schedule = models.ForeignKey(
        "event.Schedule", on_delete=models.CASCADE, related_name="presenter_schedule",
    )


class Location(models.Model):
    "Generated Model"
    name = models.TextField()
    amenities = models.TextField()
    image = models.SlugField(max_length=150,)


class MySchedule(models.Model):
    "Generated Model"
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="myschedule_user",
    )
    schedule = models.ForeignKey(
        "event.Schedule", on_delete=models.CASCADE, related_name="myschedule_schedule",
    )


class Sponsor(models.Model):
    "Generated Model"
    name = models.TextField(max_length=256,)
    logo_image = models.SlugField(max_length=150,)
    sponsor_level = models.TextField()
    presenter = models.BooleanField()
    website = models.URLField()
    location = models.ForeignKey(
        "event.Location", on_delete=models.CASCADE, related_name="sponsor_location",
    )


class Category(models.Model):
    "Generated Model"
    name = models.CharField(max_length=256,)
    description = models.TextField()


class Vendor(models.Model):
    "Generated Model"
    name = models.CharField(max_length=256,)
    logo_image = models.SlugField(max_length=150,)
    website = models.URLField()
    description = models.TextField()
    associated_name = models.TextField(null=True, blank=True,)
    location = models.ForeignKey(
        "event.Location",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="vendor_location",
    )
    category = models.ForeignKey(
        "event.Category",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="vendor_category",
    )


class Favourite(models.Model):
    "Generated Model"
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="favourite_user",
    )
    vendor = models.ForeignKey(
        "event.Vendor", on_delete=models.CASCADE, related_name="favourite_vendor",
    )


# Create your models here.
