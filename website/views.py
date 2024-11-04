from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from .models import Banners,Profile
from .serializers import BannerSerializer, UserSerializer, LoginSerializer

class BannerList(ListAPIView):
    serializer_class = BannerSerializer
    queryset = Banners.objects.all()

class SignupView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class LoginView(APIView):
    def post(self, request):
        serializer=LoginSerializer(data=request.data)

        if serializer.is_valid():
            error = None
            try:
                user=User.objects.get(username=serializer.validated_data["username"])
                profile = Profile.objects.get(user=user)
                if user.check_password(serializer.validated_data["password"]):
                    token, created = Token.objects.get_or_create(user=user)
                    _token=token.key
                else:
                    _token=None
                    error="Invalid Password."
            except user.DoesNotExist:
                _token=None
                error="Invalid Username"
            return Response({"token":_token, "error": error})



