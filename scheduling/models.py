from django.db import models


# Create your models here.
class Availability(models.Model):
    class DayOfWeek(models.IntegerChoices):
        MONDAY = 1
        TUESDAY = 2
        WEDNESDAY = 3
        THURSDAY = 4
        FRIDAY = 5
        SATURDAY = 6
        SUNDAY = 7

    user = models.ForeignKey(
        "profiles.UserProfile",
        on_delete=models.CASCADE,
    )
    day_of_week = models.IntegerField(
        choices=DayOfWeek.choices, default=DayOfWeek.MONDAY
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.day_of_week} {self.start_time}-{self.end_time}"


class MeetingProposal(models.Model):
    class Status(models.IntegerChoices):
        PENDING = 1
        ACCEPTED = 2
        DECLINED = 3

    proposer = models.ForeignKey(
        "profiles.UserProfile",
        on_delete=models.CASCADE,
        related_name="proposer",
    )
    proposee = models.ForeignKey(
        "profiles.UserProfile",
        on_delete=models.CASCADE,
        related_name="proposee",
    )
    proposed_time = models.DateTimeField()
    status = models.IntegerField(choices=Status.choices, default=Status.PENDING)

    def __str__(self):
        return f"{self.proposer.get_full_name()} proposed a meeting to {self.proposee.get_full_name()} at {self.proposed_time}"
