from rest_framework.viewsets import ModelViewSet
from .models import *
from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserRegisterSerializer


User = get_user_model()

# 회원가입
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    
# 로그인
class CustomTokenObtainPairView(TokenObtainPairView):
    pass  