from rest_framework.generics import ListAPIView, CreateAPIView
from django.contrib.auth.models import User

from .models import Banners
from .serializers import BannerSerializer, UserSerializer

class BannerList(ListAPIView):
    serializer_class = BannerSerializer
    queryset = Banners.objects.all()

class SignupView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()