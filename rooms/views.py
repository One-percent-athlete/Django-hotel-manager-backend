from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import RoomType
from .serializers import RoomTypeSerializer

class RoomTypeList(ListAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer

class RoomTypeDetail(RetrieveAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer
    lookup_field = "uuid"