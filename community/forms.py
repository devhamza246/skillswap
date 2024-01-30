from django import forms
from .models import ForumPost, CommunityEvent


class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ["content"]


class CommunityEventForm(forms.ModelForm):
    class Meta:
        model = CommunityEvent
        fields = ["title", "description", "date"]
