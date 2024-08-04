from django.urls import path
from .views import UploadCSVView, AnalyzeCSVView
from django.conf import settings
from django.conf.urls.static import static

app_name = "analysis"

urlpatterns = [
    path('', UploadCSVView.as_view(), name='upload_csv'),
    path('analyze/<int:pk>/', AnalyzeCSVView.as_view(), name='analyze_csv'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

