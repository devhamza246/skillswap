from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ["-created"]


class Availability(BaseModel):
    class DayOfWeek(models.IntegerChoices):
        MONDAY = 1
        TUESDAY = 2
        WEDNESDAY = 3
        THURSDAY = 4
        FRIDAY = 5
        SATURDAY = 6
        SUNDAY = 7

    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
    )
    day_of_week = models.IntegerField(
        choices=DayOfWeek.choices, default=DayOfWeek.MONDAY
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.day_of_week} {self.start_time}-{self.end_time}"


class MeetingProposal(BaseModel):
    class Status(models.IntegerChoices):
        PENDING = 1
        ACCEPTED = 2
        DECLINED = 3

    class Type(models.IntegerChoices):
        ONLINE = 1
        IN_PERSON = 2

    proposer = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="proposer",
    )
    proposee = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="proposee",
    )
    proposed_time = models.DateTimeField()
    meeting_type = models.IntegerField(choices=Type.choices, default=Type.IN_PERSON)
    meeting_link = models.URLField(blank=True, null=True)
    meeting_location = models.TextField(blank=True, null=True)
    status = models.IntegerField(choices=Status.choices, default=Status.PENDING)

    def __str__(self):
        return f"{self.proposer.get_full_name()} proposed a meeting to {self.proposee.get_full_name()} at {self.proposed_time}"


class ZoomAccessToken(BaseModel):
    access_token = models.TextField()

    def __str__(self):
        return self.access_token
