from rest_framework import viewsets, permissions, generics
from .models import Todo
from .serializers import TodoSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RegisterUserView(generics.CreateAPIView):
    queryset = []
    serializer_class = UserSerializer
