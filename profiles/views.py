from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from profiles.models import Skill, UserProfile


class SkillListView(ListView):
    model = Skill


class SkillDetailView(DetailView):
    model = Skill


class SkillCreateView(CreateView):
    model = Skill
    fields = ["name", "category", "description"]


class SkillUpdateView(UpdateView):
    model = Skill
    fields = ["name", "category", "description"]


class SkillDeleteView(DeleteView):
    model = Skill


class UserProfileListView(ListView):
    model = UserProfile


class UserProfileDetailView(DetailView):
    model = UserProfile


class UserProfileCreateView(CreateView):
    model = UserProfile
    fields = ["experience_level", "learning_interests"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserProfileUpdateView(UpdateView):
    model = UserProfile
    template_name = "dashboard/profile.html"
    fields = ["experience_level", "learning_interests"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserProfileDeleteView(DeleteView):
    model = UserProfile
