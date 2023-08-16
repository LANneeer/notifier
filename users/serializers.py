from rest_framework import serializers
from users.models import User
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "password", "telegram_id")

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserAuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        print(attrs)
        user = authenticate(**attrs)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
