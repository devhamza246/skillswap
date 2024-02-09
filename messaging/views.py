from typing import Any
from django.http import HttpRequest, HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from messaging.models import Message, Conversation
from django.db.models import Q


class MessageListView(ListView):
    model = Message
    template_name = "messaging/message_list.html"

    def get_context_data(self, **kwargs):
        context = super(MessageListView, self).get_context_data(**kwargs)
        context["conversations"] = Conversation.objects.all()
        return context


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    template_name = "messaging/message_form.html"
    fields = ["message", "receiver", "sender"]

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        conversation = None
        context = super().get_context_data(**kwargs)
        receiver = self.kwargs.get("receiver")
        sender = self.request.user.id
        existing_conversation = Conversation.objects.filter(
            participants__in=[sender, receiver]
        ).distinct()
        if existing_conversation.exists():
            conversation = existing_conversation.first()
        else:
            conversation = Conversation.objects.create(participants=[sender, receiver])
            conversation.save()
        context["conversation_id"] = conversation.id
        context["receiver"] = receiver
        return context


class MessageUpdateView(UpdateView):
    model = Message
    fields = ["message"]

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)


class MessageDeleteView(DeleteView):
    model = Message


class ConversationListView(ListView):
    model = Conversation
    template_name = "messaging/conversation_list.html"

    def get_context_data(self, **kwargs):
        context = super(ConversationListView, self).get_context_data(**kwargs)
        context["conversations"] = Conversation.objects.all()
        return context


class ConversationDetailView(DetailView):
    model = Conversation


class ConversationCreateView(CreateView):
    model = Conversation
    fields = ["participants"]

    def form_valid(self, form):
        form.instance.participants.add(self.request.user)
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ConversationUpdateView(UpdateView):
    model = Conversation
    fields = ["participants"]

    def form_valid(self, form):
        form.instance.participants.add(self.request.user)
        return super().form_valid(form)


class ConversationDeleteView(DeleteView):
    model = Conversation
