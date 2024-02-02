from django.db import models


# Create your models here.
class Review(models.Model):
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
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.feedback_content
