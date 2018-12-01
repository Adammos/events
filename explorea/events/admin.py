from django.contrib import admin

from .models import Event, EventRun


class EventAdmin(admin.ModelAdmin):
	list_display = ['name', 'location', 'category', 'host']
admin.site.register(Event, EventAdmin)

# Define the admin class
class EventRunAdmin(admin.ModelAdmin):
	list_display = ['event', 'date', 'time', 'price']
admin.site.register(EventRun, EventRunAdmin)


