from rest_framework import authentication
from event.models import FAQ, Location, MySchedule, Presenter, Schedule, Sponsor
from .serializers import (
    FAQSerializer,
    LocationSerializer,
    MyScheduleSerializer,
    PresenterSerializer,
    ScheduleSerializer,
    SponsorSerializer,
)
from rest_framework import viewsets


class FAQViewSet(viewsets.ModelViewSet):
    serializer_class = FAQSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = FAQ.objects.all()


class ScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = ScheduleSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Schedule.objects.all()


class PresenterViewSet(viewsets.ModelViewSet):
    serializer_class = PresenterSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Presenter.objects.all()


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Location.objects.all()


class MyScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = MyScheduleSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = MySchedule.objects.all()


class SponsorViewSet(viewsets.ModelViewSet):
    serializer_class = SponsorSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Sponsor.objects.all()
