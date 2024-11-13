"""from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth.models import User

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


#--- GET methods ----------------------
#Inicio de Sesión: Envía una solicitud POST a /api/users/login/ con el nombre de usuario y contraseña para obtener un token de autenticación.


#--- POST methods -----------------------
#Esta vista permite crear nuevos usuarios enviando un POST a /api/users/register/
"""

from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..serializers.serializer_user import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Solo los usuarios autenticados pueden acceder




