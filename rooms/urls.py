from django.urls import path
from . import views

urlpatterns = [
    path('room_types', views.RoomTypeList.as_view(), name="room_types"),
    path('room_types/<str:uuid>', views.RoomTypeDetail.as_view(), name="room_details"),
    path('room_booking', views.CreateRoomBooking.as_view(), name="room_booking"),
    path('rooms/<str:uuid>', views.RoomsList.as_view(), name="rooms"),
]
