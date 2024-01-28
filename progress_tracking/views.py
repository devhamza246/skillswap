from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from progress_tracking.models import Goal, ProgressUpdate


class GoalListView(ListView):
    model = Goal


class GoalDetailView(DetailView):
    model = Goal


class GoalCreateView(CreateView):
    model = Goal
    fields = ["description", "target_date"]


class GoalUpdateView(UpdateView):
    model = Goal
    fields = ["description", "target_date"]


class GoalDeleteView(DeleteView):
    model = Goal


class ProgressUpdateListView(ListView):
    model = ProgressUpdate


class ProgressUpdateDetailView(DetailView):
    model = ProgressUpdate


class ProgressUpdateCreateView(CreateView):
    model = ProgressUpdate
    fields = ["goal", "content"]


class ProgressUpdateUpdateView(UpdateView):
    model = ProgressUpdate
    fields = ["goal", "content"]


class ProgressUpdateDeleteView(DeleteView):
    model = ProgressUpdate
