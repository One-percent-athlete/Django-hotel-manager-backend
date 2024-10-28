from django.contrib import admin
from .models import EventBooking, EventType

admin.site.register(EventBooking)
admin.site.register(EventType)