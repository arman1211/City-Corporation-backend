from rest_framework import generics
from .models import ChatRoom, Message
from .serializers import ChatRoomSerializer, MessageSerializer

class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class ChatRoomMessagesView(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        room_id = self.kwargs['room_id']
        return Message.objects.filter(room_id=room_id).order_by('timestamp')
    
class ChatRoomCreateView(generics.CreateAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

class AllChatRoomView(generics.ListAPIView):
    queryset = ChatRoom.objects.all().order_by('-created_at')
    serializer_class= ChatRoomSerializer