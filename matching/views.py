from typing import Any
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from matching.models import Match, TrainedModel
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy


class MatchListView(LoginRequiredMixin, ListView):
    model = Match
    template_name = "matching/match_list.html"


class MatchDetailView(LoginRequiredMixin, DetailView):
    model = Match


class MatchCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Match
    fields = ["user1", "user2", "match_strength", "compatibility_score"]


class MatchUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Match
    fields = ["user1", "user2", "match_strength", "compatibility_score"]


class MatchDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Match


class TrainedModelListView(LoginRequiredMixin, ListView):
    model = TrainedModel
    template_name = "matching/trainedmodel_list.html"


class TrainedModelDetailView(LoginRequiredMixin, DetailView):
    model = TrainedModel
    template_name = "matching/trainedmodel_detail.html"


class TrainedModelCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = TrainedModel
    fields = ["model_name", "model_type", "model_parameters"]
    template_name = "matching/trainedmodel_form.html"


class TrainedModelUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = TrainedModel
    fields = ["model_name", "model_type", "model_parameters"]
    template_name = "matching/trainedmodel_form.html"


class TrainedModelDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = TrainedModel
    success_url = reverse_lazy("matching:trainedmodel_list")
    success_message = "Trained model deleted"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, self.success_message)
        return redirect(success_url)
