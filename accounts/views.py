from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import SkillAndInterest, User
from .forms import (
    LoginForm,
    SignUpForm,
    SkillAndInterestForm,
    UserInterestForm,
    UserProfileForm,
    UserSkillForm,
)
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
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
            username = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            msg = 'User created - please <a href="/login">login</a>.'
            success = True
            if user is not None:
                login(request, user)
                return redirect("accounts:add_userinterest", pk=user.pk)

        else:
            msg = "Form is not valid"
    else:
        form = SignUpForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form, "msg": msg, "success": success},
    )


def add_interest_view(request, pk):
    form = UserInterestForm(request.POST or None)

    msg = None

    if request.method == "POST":
        if form.is_valid():
            learning_interests = form.cleaned_data.get("learning_interests")
            user = User.objects.get(id=pk)
            user.learning_interests.set(learning_interests)
            user.save()
            msg = "Profile updated"
            return redirect("accounts:add_userskills", pk=pk)
        else:
            msg = "Error validating the form"

    return render(
        request, "accounts/userinterest_form.html", {"form": form, "msg": msg}
    )


def add_skills_view(request, pk):
    form = UserSkillForm(request.POST or None)

    msg = None

    if request.method == "POST":
        if form.is_valid():
            skills = form.cleaned_data.get("skills")
            user = User.objects.get(id=pk)
            user.skills.set(skills)
            user.save()
            msg = "Profile updated"
            return redirect("dashboards:home")
        else:
            msg = "Error validating the form"

    return render(request, "accounts/userskills_form.html", {"form": form, "msg": msg})


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "accounts/user_detail.html"


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = "accounts/user_update.html"
    success_url = reverse_lazy("dashboards:home")
    success_message = "Profile updated"


class SkillAndInterestListView(LoginRequiredMixin, ListView):
    model = SkillAndInterest
    template_name = "accounts/skillandinterest_list.html"


class SkillAndInterestDetailView(LoginRequiredMixin, DetailView):
    model = SkillAndInterest
    template_name = "accounts/skillandinterest_detail.html"


class SkillAndInterestCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = SkillAndInterest
    template_name = "accounts/skillandinterest_form.html"
    form_class = SkillAndInterestForm
    success_url = reverse_lazy("accounts:skillandinterest_list")
    success_message = "SkillAndInterest created"


class SkillAndInterestUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = SkillAndInterest
    template_name = "accounts/skillandinterest_form.html"
    form_class = SkillAndInterestForm
    success_url = reverse_lazy("accounts:skillandinterest_list")
    success_message = "SkillAndInterest updated"


class SkillAndInterestDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = SkillAndInterest
    success_url = reverse_lazy("accounts:skillandinterest_list")
    success_message = "SkillAndInterest deleted"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, self.success_message)
        return redirect(success_url)
