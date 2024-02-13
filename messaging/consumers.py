import json
from channels.generic.websocket import AsyncWebsocketConsumer
from accounts.models import User
from asgiref.sync import sync_to_async
from messaging.models import Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def fetch_conversation_history(self):
        # Retrieve all messages related to the conversation
        messages = await sync_to_async(Message.objects.filter)(conversation_id=self.conversation_id)

        # Serialize the messages into JSON format
        serialized_messages = [
            {
                "sender": message.sender.get_full_name(),
                "receiver": message.receiver.get_full_name(),
                "message": message.message,
            }
            for message in messages
        ]

        # Send the serialized messages to the client
        await self.send(text_data=json.dumps({"history": serialized_messages}))

    async def connect(self):
        self.conversation_id = self.scope["url_route"]["kwargs"]["conversation_id"]
        self.room_group_name = f"chat_{self.conversation_id}"
        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        # Fetch and send conversation history to the client
        await self.fetch_conversation_history()
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        sender = data["sender"]
        receiver = data["receiver"]
        message = data["message"]
        sender_obj = await sync_to_async(User.objects.get)(id=sender)
        receiver_obj = await sync_to_async(User.objects.get)(id=receiver)
        # Use sync_to_async to create the message asynchronously
        message_obj = await sync_to_async(Message.objects.create)(
            sender=sender_obj,
            receiver=receiver_obj,
            message=message,
            conversation_id=self.conversation_id,
        )
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat.message",
                "sender_id": sender,
                "sender_name": sender_obj.get_full_name(),
                "receiver_id": receiver,
                "receiver_name": receiver_obj.get_full_name(),
                "message": message,
            },
        )

    async def chat_message(self, event):
        sender_id = event["sender_id"]
        sender_name = event["sender_name"]
        receiver_id = event["receiver_id"]
        receiver_name = event["receiver_name"]
        message = event["message"]
        # Send message to WebSocket
        await self.send(
            text_data=json.dumps(
                {
                    "sender_id": sender_id,
                    "sender_name": sender_name,
                    "receiver_id": receiver_id,
                    "receiver_name": receiver_name,
                    "message": message,
                }
            )
        )
