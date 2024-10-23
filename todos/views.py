from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Todo
from .serializer import TodoSerializer


# class ListTodo(generics.ListAPIView):
#     queryset = Todo.objects.all().order_by('-id')
#     serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all().order_by('-id')
    serializer_class = TodoSerializer

class ListTodo(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Todo.objects.all().order_by('-id')
    serializer_class = TodoSerializer