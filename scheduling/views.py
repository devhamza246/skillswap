from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from scheduling.models import Availability, MeetingProposal


class AvailabilityListView(ListView):
    model = Availability


class AvailabilityCreateView(CreateView):
    model = Availability
    fields = ["user", "day_of_week", "start_time", "end_time"]


class AvailabilityDetailView(DetailView):
    model = Availability


class AvailabilityUpdateView(UpdateView):
    model = Availability
    fields = ["user", "day_of_week", "start_time", "end_time"]


class AvailabilityDeleteView(DeleteView):
    model = Availability


class MeetingProposalListView(ListView):
    model = MeetingProposal


class MeetingProposalCreateView(CreateView):
    model = MeetingProposal
    fields = ["proposer", "proposee", "proposed_time", "status"]


class MeetingProposalDetailView(DetailView):
    model = MeetingProposal


class MeetingProposalUpdateView(UpdateView):
    model = MeetingProposal
    fields = ["proposer", "proposee", "proposed_time", "status"]


class MeetingProposalDeleteView(DeleteView):
    model = MeetingProposal
