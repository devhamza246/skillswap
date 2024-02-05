from typing import Any
from django.forms.forms import BaseForm
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import Skill, User
from .forms import LoginForm, SignUpForm, SkillsForm, UserProfileForm
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = "Invalid credentials"
        else:
            msg = "Error validating the form"

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = "Form is not valid"
    else:
        form = SignUpForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form, "msg": msg, "success": success},
    )


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "accounts/user_detail.html"


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = "accounts/user_update.html"
    success_url = reverse_lazy("dashboards:home")
    success_message = "Profile updated"


class SkillsListView(LoginRequiredMixin, ListView):
    model = Skill
    template_name = "accounts/skills_list.html"


class SkillsDetailView(LoginRequiredMixin, DetailView):
    model = Skill
    template_name = "accounts/skills_detail.html"


class SkillsCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Skill
    template_name = "accounts/skills_form.html"
    form_class = SkillsForm
    success_url = reverse_lazy("accounts:skill_list")
    success_message = "Skill created"


class SkillsUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Skill
    template_name = "accounts/skills_form.html"
    form_class = SkillsForm
    success_url = reverse_lazy("accounts:skill_list")
    success_message = "Skill updated"


class SkillsDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Skill
    success_url = reverse_lazy("accounts:skill_list")
    success_message = "Skill deleted"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, self.success_message)
        return redirect(success_url)
