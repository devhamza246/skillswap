from django.db import models


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


class TrainedModel(models.Model):
    model_name = models.CharField(max_length=255)
    model_type = models.CharField(max_length=255)
    model_parameters = models.BinaryField()

    def __str__(self):
        return self.model_name
