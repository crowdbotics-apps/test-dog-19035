from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    CategoryViewSet,
    FAQViewSet,
    LocationViewSet,
    MyScheduleViewSet,
    PresenterViewSet,
    ScheduleViewSet,
    SponsorViewSet,
)

router = DefaultRouter()
router.register("faq", FAQViewSet)
router.register("schedule", ScheduleViewSet)
router.register("presenter", PresenterViewSet)
router.register("location", LocationViewSet)
router.register("myschedule", MyScheduleViewSet)
router.register("sponsor", SponsorViewSet)
router.register("category", CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
