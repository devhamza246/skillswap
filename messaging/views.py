from typing import Any
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from accounts.models import User
from messaging.models import Message, Conversation
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.db.models import Count
from messaging.serializers import MessageSerializer


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = "messaging/message_list.html"

    def get_context_data(self, **kwargs):
        context = super(MessageListView, self).get_context_data(**kwargs)
        context["conversations"] = Conversation.objects.all()
        return context


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    fields = ["message"]

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message


class ConversationListView(LoginRequiredMixin, ListView):
    model = Conversation
    template_name = "messaging/conversation_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        # Retrieve all conversations involving the current user
        conversations = Conversation.objects.filter(participants=user)

        # Collect data for other participants in each conversation
        conversations_data = []
        for conversation in conversations:
            participants_data = []
            for participant in conversation.participants.exclude(id=user.id):
                participant_data = {
                    "name": participant.get_full_name(),
                    "photo": participant.photo.url if participant.photo else None,
                }
                participants_data.append(participant_data)
            conversations_data.append(
                {
                    "conversation": conversation,
                    "participants": participants_data,
                }
            )
        # Add conversations data to the context
        context["conversations"] = conversations_data
        return context


class ConversationDetailView(LoginRequiredMixin, DetailView):
    model = Conversation
    template_name = "messaging/conversation_detail.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        conversation = self.get_object()
        messages = []
        receiver = conversation.participants.exclude(id=self.request.user.id).first()
        messages_obj = Message.objects.filter(conversation=conversation)
        if messages_obj.exists():
            messages_obj = messages_obj.order_by("created")
            messages_serializer = MessageSerializer(messages_obj, many=True)
            messages = messages_serializer.data
        context["messages"] = messages
        context["receiver"] = receiver
        return context


class ConversationCreateView(LoginRequiredMixin, CreateView):
    model = Conversation
    fields = ["participants"]


class ConversationUpdateView(LoginRequiredMixin, UpdateView):
    model = Conversation
    fields = ["participants"]

    def form_valid(self, form):
        form.instance.participants.add(self.request.user)
        return super().form_valid(form)


class ConversationDeleteView(LoginRequiredMixin, DeleteView):
    model = Conversation
