from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('scan/', views.scan_qr, name='scan_qr'),
    path('api/scan-result/', views.process_qr_scan, name='process_qr_scan'),
    path('scan-result/<uuid:qr_id>/', views.scan_result, name='scan_result'),
]