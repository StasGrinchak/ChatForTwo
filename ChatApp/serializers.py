from rest_framework import serializers
from .models import Thread, Message
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    """Serializer for user preferences"""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_active')


class MessageSerializer(serializers.ModelSerializer):

    """Serializer for message preferences"""

    class Meta:
        model = Message
        fields = '__all__'


class GetAllThreadSerializer(serializers.ModelSerializer):

    """Serializer for thread with message preferences"""

    message = MessageSerializer(read_only=True)

    class Meta:
        model = Thread
        fields = '__all__'


class ThreadSerializer(serializers.ModelSerializer):

    """Serializer for thread with participants preferences"""

    participants = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Thread
        fields = ('participants', 'created', 'updated', )

    def create(self, validated_data):
        
        return super().create(validated_data)

