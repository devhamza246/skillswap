from django.http import HttpRequest, HttpResponse
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from community.forms import CommunityEventForm, ForumPostForm
from community.models import CommunityEvent, ForumPost
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class ForumPostListView(LoginRequiredMixin, ListView):
    model = ForumPost


class ForumPostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ForumPost
    template_name = "community/forumpost_form.html"
    form_class = ForumPostForm
    success_url = reverse_lazy("community:forumpost_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ForumPostDetailView(LoginRequiredMixin, DetailView):
    model = ForumPost


class ForumPostUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ForumPost
    form_class = ForumPostForm


class ForumPostDeleteView(LoginRequiredMixin, DeleteView):
    model = ForumPost


class CommunityEventListView(LoginRequiredMixin, ListView):
    model = CommunityEvent


class CommunityEventCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = CommunityEvent
    template_name = "community/communityevent_form.html"
    form_class = CommunityEventForm
    success_url = reverse_lazy("community:communityevent_list")

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super().form_valid(form)


class CommunityEventDetailView(LoginRequiredMixin, DetailView):
    model = CommunityEvent


class CommunityEventUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CommunityEvent
    form_class = CommunityEventForm


class CommunityEventDeleteView(LoginRequiredMixin, DeleteView):
    model = CommunityEvent
