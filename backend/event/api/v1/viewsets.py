from rest_framework import authentication
from event.models import (
    Category,
    FAQ,
    Location,
    MySchedule,
    Presenter,
    Schedule,
    Sponsor,
    Vendor,
)
from .serializers import (
    CategorySerializer,
    FAQSerializer,
    LocationSerializer,
    MyScheduleSerializer,
    PresenterSerializer,
    ScheduleSerializer,
    SponsorSerializer,
    VendorSerializer,
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


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Category.objects.all()


class VendorViewSet(viewsets.ModelViewSet):
    serializer_class = VendorSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Vendor.objects.all()
