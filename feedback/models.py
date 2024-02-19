from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ["-created"]


# Create your models here.
class Review(BaseModel):
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
    rating = models.IntegerField()
    feedback_content = models.TextField()

    def __str__(self):
        return self.feedback_content
