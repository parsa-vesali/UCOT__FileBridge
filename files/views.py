"""
Views for file management.

This module contains API views for uploading, deleting, and listing files.
"""

from rest_framework import generics, permissions

from .models import File
from .serializers import FileSerializer


class FileUploadView(generics.CreateAPIView):
    """
    API view for teachers to upload files.

    Only authenticated users can upload files.
    The file is automatically associated with the current user.
    """

    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Save the file with the current user as the teacher.

        Args:
            serializer: The serializer instance containing validated data.
        """
        serializer.save(teacher=self.request.user)


class FileDeleteView(generics.DestroyAPIView):
    """
    API view for teachers to delete their own files.

    Only authenticated users can delete files, and they can only
    delete files they have uploaded themselves.
    """

    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Filter queryset to only include files uploaded by the current user.

        Returns:
            QuerySet: Files belonging to the current user.
        """
        return File.objects.filter(teacher=self.request.user)


class FileListView(generics.ListAPIView):
    """
    API view for listing all uploaded files.

    This is a public view accessible to all users.
    """

    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [permissions.AllowAny]
