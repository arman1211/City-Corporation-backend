from django.db import models
from user_authentication.models import User

class ChatRoom(models.Model):
    citizen = models.ForeignKey(User,related_name='citizen_chatroom',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    room = models.ForeignKey(ChatRoom, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)