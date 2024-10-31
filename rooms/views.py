from rest_framework.generics import ListAPIView
from .models import RoomType, RoomImage
from .serializers import RoomTypeSerializer, RoomImageSerializer

class RoomTypeList(ListAPIView):
    serializer_class = RoomTypeSerializer
    queryset = RoomType.objects.all()

class RoomImageList(ListAPIView):
    serializer_class = RoomImageSerializer
    queryset = RoomImage.objects.all()