from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from accounts.models import Skill
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

User = get_user_model()


class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Email", "class": "form-control"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        )
    )


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "First Name", "class": "form-control"}
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Last Name", "class": "form-control"}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password check", "class": "form-control"}
        )
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password1", "password2")


class UserProfileForm(forms.ModelForm):
    photo = forms.ImageField(
        label="Profile Photo",
        required=False,  # Set this to True if the photo is mandatory
        widget=forms.FileInput(attrs={"class": "form-control"}),
    )
    skills = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
        choices=Skill.objects.all().values_list("id", "name"),
    )

    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "address",
            "city",
            "country",
            "photo",
            "skills",
            "experience_level",
            "learning_interests",
        ]
        widgets = {
            "email": forms.EmailInput(
                attrs={"class": "form-control", "readonly": True}
            ),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "country": CountrySelectWidget(
                attrs={"class": "form-control"},
                layout="{widget}",
            ),
            "experience_level": forms.Select(attrs={"class": "form-control"}),
            "learning_interests": forms.Textarea(attrs={"class": "form-control"}),
        }


class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = [
            "name",
            "category",
            "description",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
        }
