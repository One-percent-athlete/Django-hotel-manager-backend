from rest_framework import serializers
from .models import RoomType, RoomImage, RoomBooking

class RoomTypeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ["image"]

class RoomTypeSerializer(serializers.ModelSerializer):
    room_type_image = RoomTypeImageSerializer(many=True)
    class Meta:
        model = RoomType
        fields = ["uuid", "title", "details", "room_type_image", "price_per_night"]

class RoomBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomBooking
        fields = ["room_number", "user", "booking_date", "total_guest", "checkin_date", "checkout_date", "price", "booking_details"]