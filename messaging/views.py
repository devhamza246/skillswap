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
    template_name = "messaging/message_form.html"
    fields = ["message", "receiver", "sender"]

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        sender = self.request.user.id
        receiver_id = self.kwargs.get("receiver")
        conversation_id = self.kwargs.get("conversation")
        messages = []
        if receiver_id:
            receiver = get_object_or_404(User, id=receiver_id)
            existing_conversations = (
                Conversation.objects.filter(participants__in=[sender, receiver_id])
                .annotate(num_participants=Count("participants"))
                .filter(num_participants=2)
            )

            if existing_conversations.exists():
                conversation_obj = existing_conversations.first()
            else:
                conversation_obj = Conversation.objects.create()
                conversation_obj.participants.add(sender, receiver_id)

        elif conversation_id:
            conversation_obj = get_object_or_404(Conversation, id=conversation_id)
            receiver = conversation_obj.participants.exclude(id=sender).first()

        messages_obj = Message.objects.filter(conversation=conversation_obj)
        if messages_obj.exists():
            messages_obj = messages_obj.order_by("created")
            messages_serializer = MessageSerializer(messages_obj, many=True)
            messages = messages_serializer.data

        context["conversation_id"] = conversation_obj.id
        context["receiver"] = receiver
        context["messages"] = messages
        return context


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
