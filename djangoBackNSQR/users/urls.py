from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.view_register import RegisterView
from .views.view_user import UserViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'users', UserViewSet)  # Esto registra el ViewSet de usuarios

urlpatterns = [
    path('', include(router.urls)),  # Rutas generadas por el DefaultRouter
    path('register/', RegisterView.as_view(), name='register'),  # Registro
    #path('login/', obtain_auth_token, name='login'),  # Login (obtención de token)
]
