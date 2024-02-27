from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from scheduling.forms import AvailabilityForm, MeetingProposalForm
from scheduling.models import Availability, MeetingProposal
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin



class AvailabilityListView(LoginRequiredMixin, ListView):
    model = Availability


class AvailabilityCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Availability
    form_class = AvailabilityForm
    fields = ["user", "day_of_week", "start_time", "end_time"]


class AvailabilityDetailView(LoginRequiredMixin, DetailView):
    model = Availability


class AvailabilityUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Availability
    fields = ["user", "day_of_week", "start_time", "end_time"]


class AvailabilityDeleteView(LoginRequiredMixin, DeleteView):
    model = Availability


class MeetingProposalListView(LoginRequiredMixin, ListView):
    model = MeetingProposal


class MeetingProposalCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = MeetingProposal
    form_class = MeetingProposalForm
    template_name = "scheduling/meetingproposal_form.html"
    success_url = "scheduling:meetingproposal_list"
    
    def post(self, request, *args, **kwargs):
        print(request.POST)
        return super().post(request, *args, **kwargs)


class MeetingProposalDetailView(LoginRequiredMixin, DetailView):
    model = MeetingProposal


class MeetingProposalUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = MeetingProposal
    fields = ["proposer", "proposee", "proposed_time", "status"]


class MeetingProposalDeleteView(LoginRequiredMixin, DeleteView):
    model = MeetingProposal
