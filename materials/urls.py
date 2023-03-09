from django.urls import path
from .views import subject_list, material_list,download_file
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('subjects/', subject_list, name='subject_list'),
    path('<int:subject_id>/', material_list, name='material_list'),
    path('download/<str:file_name>/', download_file, name='download_file'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

