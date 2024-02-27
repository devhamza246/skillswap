from rest_framework import serializers
from accounts.models import User


class MatchUserSerializer(serializers.ModelSerializer):
    skills = serializers.SerializerMethodField()
    learning_interests = serializers.SerializerMethodField()
    experience_level = serializers.CharField(source="get_experience_level_display")

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "photo",
            "email",
            "skills",
            "experience_level",
            "learning_interests",
        ]

    def get_skills(self, obj):
        return ", ".join([skill.name for skill in obj.skills.all()])

    def get_learning_interests(self, obj):
        return ", ".join([learning_interest.name for learning_interest in obj.learning_interests.all()])
