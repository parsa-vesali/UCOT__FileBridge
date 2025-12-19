"""
File upload models for the application.

This module contains models related to file management and uploads.
"""

from django.conf import settings
from django.db import models


class File(models.Model):
    """
    Model representing an uploaded file by a teacher.

    Attributes:
        teacher: Foreign key to the user who uploaded the file.
        title: Title of the uploaded file.
        file: The actual file being uploaded.
        uploaded_at: Timestamp when the file was uploaded.
    """

    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='uploaded_files',
        verbose_name='Teacher'
    )
    title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Title'
    )
    file = models.FileField(
        upload_to='uploads/',
        verbose_name='File'
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Uploaded At'
    )

    class Meta:
        """Meta options for the File model."""

        ordering = ['-uploaded_at']
        verbose_name = 'File'
        verbose_name_plural = 'Files'

    def __str__(self):
        """Return string representation of the file."""
        return self.title if self.title else f"File {self.id}"