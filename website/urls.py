from django.urls import path
from . import views

urlpatterns = [
    path('banners', views.BannerList.as_view(), name="banners"),
    path('signup', views.SignupView.as_view(), name="signup"),
]
