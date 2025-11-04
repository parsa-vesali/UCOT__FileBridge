from django.contrib import admin
from django.urls import path
from accounts.views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from files.views import FileUploadView, FileDeleteView, FileListView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterView.as_view()),
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/files/', FileListView.as_view()),           # student view (public)
    path('api/files/upload/', FileUploadView.as_view()),  # teacher upload
    path('api/files/<int:pk>/delete/', FileDeleteView.as_view()),  # teacher delete
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

