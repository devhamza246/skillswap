from django.db import models


# Create your models here.
class Match(models.Model):
    user1 = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="user1",
    )
    user2 = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="user2",
    )
    match_strength = models.FloatField(default=0.0)
    compatibility_score = models.FloatField(default=0.0)
