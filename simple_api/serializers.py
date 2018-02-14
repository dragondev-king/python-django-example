"""Simple API Serializers"""

from rest_framework import serializers
from simple_api.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    """Todo Model Serializer"""

    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'is_active', 'created_at', 'priority')
