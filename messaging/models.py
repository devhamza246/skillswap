from django.db import models


# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(
        "profiles.UserProfile",
        on_delete=models.CASCADE,
        related_name="sender",
    )
    receiver = models.ForeignKey(
        "profiles.UserProfile",
        on_delete=models.CASCADE,
        related_name="receiver",
    )
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message


class Conversation(models.Model):
    participants = models.ManyToManyField(
        "profiles.UserProfile",
        blank=True,
    )
    last_message = models.ForeignKey(
        "messaging.Message",
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.last_message
