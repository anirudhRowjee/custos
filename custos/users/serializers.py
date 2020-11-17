from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile


class UserSerializer(serializers.ModelSerializer):
    # serializer for the User object

    class Meta:
        model = User
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    # serializer for Profile Object,

    class Meta:
        model = Profile
        fields = "__all__"
