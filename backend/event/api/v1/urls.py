from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    CategoryViewSet,
    FAQViewSet,
    FavouriteViewSet,
    LocationViewSet,
    MyScheduleViewSet,
    PresenterViewSet,
    ScheduleViewSet,
    SponsorViewSet,
    VendorViewSet,
)

router = DefaultRouter()
router.register("faq", FAQViewSet)
router.register("schedule", ScheduleViewSet)
router.register("presenter", PresenterViewSet)
router.register("location", LocationViewSet)
router.register("myschedule", MyScheduleViewSet)
router.register("sponsor", SponsorViewSet)
router.register("category", CategoryViewSet)
router.register("vendor", VendorViewSet)
router.register("favourite", FavouriteViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
