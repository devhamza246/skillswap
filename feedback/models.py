from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ["-created"]


# Create your models here.
class Review(BaseModel):
    class Rating(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    reviewer = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="reviewer",
    )
    reviewed_user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="reviewed_user",
    )
    rating = models.IntegerField(choices=Rating.choices)
    feedback_content = models.TextField()

    def __str__(self):
        return self.feedback_content
