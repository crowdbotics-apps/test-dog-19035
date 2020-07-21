from django.contrib import admin
from .models import (
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

admin.site.register(FAQ)
admin.site.register(Schedule)
admin.site.register(Presenter)
admin.site.register(Location)
admin.site.register(MySchedule)
admin.site.register(Sponsor)
admin.site.register(Category)
admin.site.register(Vendor)
admin.site.register(Favourite)

# Register your models here.
