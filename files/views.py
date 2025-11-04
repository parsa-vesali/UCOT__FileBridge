from rest_framework import generics, permissions
from .models import File
from .serializers import FileSerializer

# Teacher uploads file
class FileUploadView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)


# Teacher deletes own file
class FileDeleteView(generics.DestroyAPIView):
    queryset = File.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return File.objects.filter(teacher=self.request.user)


# All users see the files (public)
class FileListView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
