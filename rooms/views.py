from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .models import RoomType, RoomBooking
from .serializers import RoomTypeSerializer, RoomBookingSerializer

class RoomTypeList(ListAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer

class RoomTypeDetail(RetrieveAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer
    lookup_field = "uuid"

class CreateRoomBooking(CreateAPIView):
    queryset = RoomBooking.objects.all()
    serializer_class = RoomBookingSerializer