from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["reviewer", "reviewed_user", "rating", "feedback_content"]
