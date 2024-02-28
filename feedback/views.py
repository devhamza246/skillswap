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
from django.urls import reverse_lazy


class ReviewListView(LoginRequiredMixin, ListView):
    model = Review


class ReviewCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Review


class ReviewDetailView(LoginRequiredMixin, DetailView):
    model = Review


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    fields = ["rating", "feedback_content"]
