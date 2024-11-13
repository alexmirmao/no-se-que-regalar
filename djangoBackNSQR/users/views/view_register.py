from rest_framework import generics
from ..serializers.serializer_user import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.views import obtain_auth_token


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
