from django.urls import path
from .views import MessageCreateView,ChatRoomCreateView, ChatRoomMessagesView,AllChatRoomView

urlpatterns = [
    path('chat-room/<int:room_id>/messages/', ChatRoomMessagesView.as_view(), name='chat-room-messages'),
    path('message/send/', MessageCreateView.as_view(), name='message-create'),
    path('chat-room/', ChatRoomCreateView.as_view(), name='chat-room-create'),
    path('chat-room/list', AllChatRoomView.as_view(), name='chat-room-list'),
    

]