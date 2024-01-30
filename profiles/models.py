from django.db import models

from accounts.models import User
from messaging.models import Conversation


class Skill(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    class Levels(models.IntegerChoices):
        ENTRY_LEVEL = 1
        INTERMEDIATE = 2
        MID_LEVEL = 3
        SENIOR = 4

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    conversations = models.ManyToManyField(Conversation, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    experience_level = models.IntegerField(
        choices=Levels.choices, default=Levels.ENTRY_LEVEL
    )
    learning_interests = models.TextField(blank=True)

    def __str__(self):
        return self.user.get_full_name()
