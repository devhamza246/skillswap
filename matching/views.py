from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from matching.models import Match


class MatchListView(ListView):
    model = Match


class MatchDetailView(DetailView):
    model = Match


class MatchCreateView(CreateView):
    model = Match
    fields = ["user1", "user2", "match_strength", "compatibility_score"]


class MatchUpdateView(UpdateView):
    model = Match
    fields = ["user1", "user2", "match_strength", "compatibility_score"]


class MatchDeleteView(DeleteView):
    model = Match
