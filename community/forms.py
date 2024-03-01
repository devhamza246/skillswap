from django import forms
from .models import ForumPost, CommunityEvent


class ForumPostForm(forms.ModelForm):

    class Meta:
        model = ForumPost
        fields = [
            "title",
            "content",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
        }


class CommunityEventForm(forms.ModelForm):
    class Meta:
        model = CommunityEvent
        fields = ["title", "description", "date"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
        }
