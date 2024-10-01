from django.shortcuts import render
from .serializers import ContactSerializer
from .models import ContactModel
from rest_framework import generics
# Create your views here.

class ContactPostView(generics.CreateAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer

class ContactGetView(generics.ListAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer