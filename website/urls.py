from django.urls import path
from . import views

urlpatterns = [
    path('banners', views.BannerList.as_view(), name="banners"),
    path('signup', views.SignupView.as_view(), name="signup"),
    path('login', views.LoginView.as_view(), name="login"),
    path('email_validation', views.EmailValidationView.as_view(), name="email_validation"),
    path('code_validation', views.CodeValidationView.as_view(), name="code_validation"),
]
