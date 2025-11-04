from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from accounts.views import RegisterView
from files.views import FileUploadView, FileDeleteView, FileListView


# Swagger Schema Configuration
schema_view = get_schema_view(
    openapi.Info(
        title="Teacher Files API",
        default_version='v1',
        description="API documentation for teacher file upload system",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


# Routes
urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Auth
    path('api/register/', RegisterView.as_view()),
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),

    # Files
    path('api/files/', FileListView.as_view()),           
    path('api/files/upload/', FileUploadView.as_view()),  
    path('api/files/<int:pk>/delete/', FileDeleteView.as_view()),  

    # Swagger
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


# Media files serving
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
