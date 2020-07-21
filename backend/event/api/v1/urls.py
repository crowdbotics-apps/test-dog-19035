from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    FAQViewSet,
    LocationViewSet,
    MyScheduleViewSet,
    PresenterViewSet,
    ScheduleViewSet,
)

router = DefaultRouter()
router.register("faq", FAQViewSet)
router.register("schedule", ScheduleViewSet)
router.register("presenter", PresenterViewSet)
router.register("location", LocationViewSet)
router.register("myschedule", MyScheduleViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
