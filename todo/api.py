from .models import *
from rest_framework import viewsets, permissions
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permissions_classes = [
        permissions.AllowAny
    ]
