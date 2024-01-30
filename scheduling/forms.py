from django import forms
from .models import Availability, MeetingProposal


class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ["day_of_week", "start_time", "end_time"]


class MeetingProposalForm(forms.ModelForm):
    class Meta:
        model = MeetingProposal
        fields = ["proposee", "proposed_time"]
