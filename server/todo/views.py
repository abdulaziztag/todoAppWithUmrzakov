from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.views import APIView

from .models import Todo
from .serializers import TodoSerializer, PostTodoSerializer

class TodoListView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class AddTaskView(APIView):
    def post(self, request):
        task = PostTodoSerializer(request.data)
        if task.is_valid():
            task.save()
        return Response(status=201)