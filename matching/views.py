from django.views.generic import (
    ListView,
)
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models import User


class MatchListView(LoginRequiredMixin, ListView):
    model = User
    template_name = "matching/match_list.html"
