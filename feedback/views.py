from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from feedback.models import Review


class ReviewListView(ListView):
    model = Review


class ReviewCreateView(CreateView):
    model = Review
    fields = ["rating", "feedback_content"]


class ReviewDetailView(DetailView):
    model = Review


class ReviewUpdateView(UpdateView):
    model = Review
    fields = ["rating", "feedback_content"]


class ReviewDeleteView(DeleteView):
    model = Review
