from django.urls import path
from .views import TodoListView, TodoDetailView, AddTaskView

urlpatterns = [
    path('get_all/', TodoListView.as_view()),
    path('<int:pk>/', TodoDetailView.as_view()),
    path('post/', AddTaskView.as_view()),
]
