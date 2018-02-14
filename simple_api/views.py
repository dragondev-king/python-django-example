"""Simple API View Classes"""

from __future__ import unicode_literals

from rest_framework import generics

from simple_api.models import Todo
from simple_api.serializers import TodoSerializer

class TodoList(generics.ListCreateAPIView):
    """ Handles List and Create actions """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Handles Read, Update and Delete actions """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
