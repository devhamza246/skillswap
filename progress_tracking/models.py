from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ["-created"]


class Goal(BaseModel):
    class Status(models.IntegerChoices):
        NOT_STARTED = 1
        IN_PROGRESS = 2
        COMPLETED = 3

    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
    )
    description = models.TextField()
    target_date = models.DateField()
    status = models.IntegerField(choices=Status.choices, default=Status.NOT_STARTED)

    def __str__(self):
        return self.description


class ProgressUpdate(BaseModel):
    goal = models.ForeignKey(
        "progress_tracking.Goal",
        on_delete=models.CASCADE,
    )
    content = models.TextField()

    def __str__(self):
        return self.content
