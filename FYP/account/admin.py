from django.contrib import admin
from .models import City, due

admin.site.site_header = "RideSafely Admin Panel"
admin.site.register(City)
admin.site.register(due)