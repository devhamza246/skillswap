from django.db import models


# Create your models here.
class ForumPost(models.Model):
    author = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
    )
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class CommunityEvent(models.Model):
    organizer = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title
