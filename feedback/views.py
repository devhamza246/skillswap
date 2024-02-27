from typing import Any
from django.http import HttpRequest, HttpResponse
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from feedback.forms import ReviewForm
from django.contrib.messages.views import SuccessMessageMixin
from feedback.models import Review
from django.contrib.auth.mixins import LoginRequiredMixin


class ReviewListView(LoginRequiredMixin, ListView):
    model = Review


class ReviewCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Review
    form_class = ReviewForm
    success_url = "dashboards:home"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviewed_user = self.kwargs.get("reviewed_user")
        context["reviewed_user"] = reviewed_user
        return context


class ReviewDetailView(LoginRequiredMixin, DetailView):
    model = Review


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    fields = ["rating", "feedback_content"]


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
