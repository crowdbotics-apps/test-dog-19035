from rest_framework import serializers
from event.models import FAQ, Location, MySchedule, Presenter, Schedule


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
