from django.contrib.auth import get_user_model
from rest_framework import serializers

from accounts.models import SkillAndInterest

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            email=validated_data["email"], password=validated_data["password"]
        )
        return user


class SkillAndInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillAndInterest
        fields = "__all__"
