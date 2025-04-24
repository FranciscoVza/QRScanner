from django.contrib import admin
from .models import QRCode, QRScan

@admin.register(QRCode)
class QRCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'created_at')
    search_fields = ('content',)
    readonly_fields = ('id', 'created_at')

@admin.register(QRScan)
class QRScanAdmin(admin.ModelAdmin):
    list_display = ('id', 'qr_code', 'scanned_at', 'ip_address')
    list_filter = ('scanned_at',)
    readonly_fields = ('scanned_at',)