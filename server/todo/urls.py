from django.urls import path
from .views import TodoListView, TodoDetailView

urlpatterns = [
    path('all/', TodoListView.as_view()),
    path('<int:pk>/', TodoDetailView.as_view()),
    path('add/', TodoListView.as_view()),
]
