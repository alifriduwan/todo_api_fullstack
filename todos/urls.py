from django.urls import path

from .views import ListTodo, DetailTodo

urlpatterns = [
    # /api/todos/<id>
    path('<int:pk>/', DetailTodo.as_view(), name='todo_detail'),
    
    path('', ListTodo.as_view(), name='todo_list'),
]
