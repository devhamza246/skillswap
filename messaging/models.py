from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created"]


# Create your models here.
class Message(BaseModel):
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

    def __str__(self):
        return self.message


class Conversation(BaseModel):
    participants = models.ManyToManyField("accounts.User", blank=True)
