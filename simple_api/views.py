"""Simple API View Classes"""

from __future__ import unicode_literals

from rest_framework import generics
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from simple_api.models import Todo
from simple_api.serializers import TodoSerializer

class TodoList(generics.ListCreateAPIView):
    """ Handles List and Create actions """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication)
    permission_classes = (IsAuthenticated,)

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Handles Read, Update and Delete actions """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
