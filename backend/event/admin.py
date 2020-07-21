from django.contrib import admin
from .models import Category, FAQ, Location, MySchedule, Presenter, Schedule, Sponsor

admin.site.register(FAQ)
admin.site.register(Schedule)
admin.site.register(Presenter)
admin.site.register(Location)
admin.site.register(MySchedule)
admin.site.register(Sponsor)
admin.site.register(Category)

# Register your models here.
