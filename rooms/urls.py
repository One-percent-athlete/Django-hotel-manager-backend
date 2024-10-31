from django.urls import path
from . import views

urlpatterns = [
    path('room_types', views.RoomTypeList.as_view(), name="room_types"),
    path('room_images', views.RoomImageList.as_view(), name="room_images"),
]
