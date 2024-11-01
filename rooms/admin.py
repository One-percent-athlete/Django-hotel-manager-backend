from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import format_html

from .models import RoomType, Room, RoomBooking, Payment, Gallery, RoomImage

admin.site.register(Room)
admin.site.register(RoomBooking)
admin.site.register(Payment)
admin.site.register(Gallery)

class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 1

class RoomTypeAdmin(admin.ModelAdmin):
    inlines = [RoomImageInline]
    list_display = ["title", "first_image"]

    def first_image(self, obj):
        first_image = obj.room_type_image.first()
        if first_image:
            return u"<img src='%s' width='50 />" % first_image.image.url
    first_image.allow_tags=True

admin.site.register(RoomType, RoomTypeAdmin)
admin.site.register(RoomImage)