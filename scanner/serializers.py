from rest_framework import serializers
from .models import QRCode, QRScan

class QRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRCode
        fields = ['id', 'content', 'created_at']

class QRScanSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRScan
        fields = ['id', 'qr_code', 'scanned_at', 'user_agent', 'ip_address']