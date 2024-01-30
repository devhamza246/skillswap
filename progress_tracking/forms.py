from django import forms
from .models import Goal, ProgressUpdate


class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ["description", "target_date", "status"]


class ProgressUpdateForm(forms.ModelForm):
    class Meta:
        model = ProgressUpdate
        fields = ["content"]
