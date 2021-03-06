from rest_framework import serializers
from event.models import (
    Category,
    FAQ,
    Favourite,
    Location,
    MySchedule,
    Presenter,
    Schedule,
    Sponsor,
    Vendor,
)


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = "__all__"


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"


class PresenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presenter
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class MyScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MySchedule
        fields = "__all__"


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"


class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = "__all__"
