from django.db import models


# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="sender",
    )
    receiver = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="receiver",
    )
    conversation = models.ForeignKey(
        "messaging.Conversation",
        blank=True,
        on_delete=models.CASCADE,
    )
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message


class Conversation(models.Model):
    participants = models.ManyToManyField(
        "accounts.User",
        blank=True,
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.last_message
