from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from community.forms import CommunityEventForm, ForumPostForm
from community.models import CommunityEvent, ForumPost


class ForumPostListView(ListView):
    model = ForumPost


class ForumPostCreateView(CreateView):
    model = ForumPost
    form_class = ForumPostForm
    fields = ["content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ForumPostDetailView(DetailView):
    model = ForumPost


class ForumPostUpdateView(UpdateView):
    model = ForumPost
    fields = ["content"]


class ForumPostDeleteView(DeleteView):
    model = ForumPost


class CommunityEventListView(ListView):
    model = CommunityEvent


class CommunityEventCreateView(CreateView):
    model = CommunityEvent
    form_class = CommunityEventForm
    fields = ["title", "description", "date"]

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super().form_valid(form)


class CommunityEventDetailView(DetailView):
    model = CommunityEvent


class CommunityEventUpdateView(UpdateView):
    model = CommunityEvent
    fields = ["title", "description", "date"]


class CommunityEventDeleteView(DeleteView):
    model = CommunityEvent
