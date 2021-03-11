from rest_framework import serializers

from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'created', 'done')

class PostTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title',)