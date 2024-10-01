from rest_framework import serializers
from .models import ChatRoom, Message

class ChatRoomSerializer(serializers.ModelSerializer):
    last_message = serializers.SerializerMethodField()
    class Meta:
        model = ChatRoom
        fields = ['id', 'citizen', 'created_at','last_message']
    def get_last_message(self, obj):
        last_message = Message.objects.filter(room=obj).order_by('-timestamp').first()
        if last_message:
            return {
                'content': last_message.content,
                'timestamp': last_message.timestamp,
                'sender_name': last_message.sender.username
            }
        return None

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'room', 'sender', 'content', 'timestamp']
    