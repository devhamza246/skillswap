from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ["-created"]


# Create your models here.
class ForumPost(BaseModel):
    author = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
    )
    content = models.TextField()

    def __str__(self):
        return self.content


class CommunityEvent(BaseModel):
    organizer = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title
