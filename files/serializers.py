"""
Serializers for file management.

This module contains serializers for converting File model instances
to and from JSON representations.
"""

from rest_framework import serializers

from .models import File


class FileSerializer(serializers.ModelSerializer):
    """
    Serializer for the File model.

    Serializes file instances with id, title, file path, and upload timestamp.
    The teacher field is set automatically in the view and is read-only here.
    """

    teacher_name = serializers.CharField(
        source='teacher.get_full_name',
        read_only=True
    )

    class Meta:
        """Meta options for FileSerializer."""

        model = File
        fields = ['id', 'title', 'file', 'uploaded_at', 'teacher_name']
        read_only_fields = ['id', 'uploaded_at', 'teacher_name']

    def validate_title(self, value):
        """
        Validate the title field.

        Args:
            value: The title value to validate.

        Returns:
            str: The validated title.

        Raises:
            serializers.ValidationError: If title is empty or only whitespace.
        """
        if value and not value.strip():
            raise serializers.ValidationError(
                "Title cannot be empty or contain only whitespace."
            )
        return value.strip() if value else value