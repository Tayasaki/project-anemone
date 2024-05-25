from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            is_superuser=validated_data['is_superuser'],
            is_staff=validated_data['is_superuser'],
        )
        return user

    class Meta:
        model = User
        fields = ['pk', 'username', 'password', 'email', 'is_superuser']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'zip', 'rating')


class LocationCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationComment
        fields = ('id', 'comment', 'location', 'user')


class LocationRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationRating
        fields = ('id', 'rating', 'location', 'user')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'lan', 'user', 'location', 'date', 'capacity', 'current_capacity')


class EventRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRegistration
        fields = ('id', 'event', 'user')
