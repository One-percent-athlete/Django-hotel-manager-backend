from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Banners
from .serializers import BannerSerializer

class BannerList(ListAPIView):
    serializer_class = BannerSerializer
    queryset = Banners.objects.all()