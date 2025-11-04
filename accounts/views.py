from rest_framework import generics
from .models import Teacher
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = RegisterSerializer
