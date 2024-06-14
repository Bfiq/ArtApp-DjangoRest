from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Board, Pin, BoardPin, Tag

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'

class PinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pin
        fields = '__all__'

class BoardPinSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardPin
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'