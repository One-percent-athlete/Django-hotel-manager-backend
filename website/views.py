from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from .models import Banners,Profile
from .serializers import BannerSerializer, UserSerializer, LoginSerializer, EmailValidationSerializer, CodeValidationSerializer, ChangePasswordSerializer

class BannerList(ListAPIView):
    serializer_class = BannerSerializer
    queryset = Banners.objects.all()

class CustomSignupView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class CustomLoginView(APIView):
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

class EmailValidationView(APIView):
    def post(self, request):
        serializer=EmailValidationSerializer(data=request.data)

        if serializer.is_valid():
            error = None
            try:
                user=User.objects.get(email=serializer.validated_data["email"])
            except user.DoesNotExist:
                error="Invalid Email"
            return Response({"error": error})
        
class CodeValidationView(APIView):
    def post(self, request):
        serializer=CodeValidationSerializer(data=request.data)

        if serializer.is_valid():
            error = None
            if serializer.validated_data["code"] != "1234":
                error = 'Code Not Correct'
            else:
                return Response({"error": error})

class CustomChangePasswordView(APIView):
    def post(self, request):
        serializer=ChangePasswordSerializer(data=request.data)

        error = None
        if serializer.is_valid():
            try:
                user=User.objects.get(email=serializer.validated_data["email"])
                if user:
                    user.password=serializer.validated_data["password"]
                    user.save()
                else:
                    error="Invalid Infomation"
            except user.DoesNotExist:
                error="Invalid Email"
        return Response({"error": error})


