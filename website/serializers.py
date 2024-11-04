from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Banners, Profile

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banners
        fields = ["id", "title", "image"]

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["phone"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name","last_name","username","password","email"]

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        password = validated_data.pop("password")
        user.set_password(password)
        user.save()
        # profile_data = validated_data.pop("profile")
        # profile = Profile.objects.filter(user=user).update(phone=profile_data["phone"])
        # profile.save()
        return user
    

class LoginSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ["username","password"]
        username = serializers.CharField()
        password = serializers.CharField()
