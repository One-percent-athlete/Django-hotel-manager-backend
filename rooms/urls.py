from django.urls import path
from . import views

urlpatterns = [
    path('room_types', views.RoomTypeList.as_view(), name="room_types"),
    path('room_types/<int:pk>', views.RoomTypeDetail.as_view(), name="room_details"),
]
