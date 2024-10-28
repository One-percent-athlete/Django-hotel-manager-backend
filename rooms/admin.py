from django.contrib import admin
from .models import RoomType, Room, Booking, Payment, Gallery, RoomImage

admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Gallery)
admin.site.register(RoomImage)