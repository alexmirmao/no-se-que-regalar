from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password']  # Excluir 'username'
    
    def create(self, validated_data):
        # Crear el usuario utilizando el email como username
        user = User.objects.create_user(
            username=validated_data['email'],  # Usa el email como username
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user