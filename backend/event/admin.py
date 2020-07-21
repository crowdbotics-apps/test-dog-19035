from django.contrib import admin
from .models import FAQ, Location, MySchedule, Presenter, Schedule

admin.site.register(FAQ)
admin.site.register(Schedule)
admin.site.register(Presenter)
admin.site.register(Location)
admin.site.register(MySchedule)

# Register your models here.
