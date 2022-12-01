from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name',
                  'last_name', 'password', 'is_active', 'is_staff'
                  )
        extra_kwargs = {
            'password': {'write_only': True}
        }