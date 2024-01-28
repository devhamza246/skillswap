from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from messaging.models import Message, Conversation


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
    fields = ["message"]

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)


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


class ConversationUpdateView(UpdateView):
    model = Conversation
    fields = ["participants"]

    def form_valid(self, form):
        form.instance.participants.add(self.request.user)
        return super().form_valid(form)


class ConversationDeleteView(DeleteView):
    model = Conversation
