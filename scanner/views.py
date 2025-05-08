from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import QRCode, QRScan
from .serializers import QRCodeSerializer, QRScanSerializer
import json

def index(request):
    """Página principal con interfaz para escanear QR"""
    return render(request, 'scanner/index.html')

def qr_codes_list(request):
    """Vista para mostrar la lista de códigos QR en una tabla"""
    qr_codes = QRCode.objects.all()
    return render(request, 'scanner/qr_codes_list.html', {'qr_codes': qr_codes})


def scan_qr(request):
    """Página con el escáner de QR usando la cámara del teléfono"""
    return render(request, 'scanner/scan.html')

def scan_result(request, qr_id):
    """Muestra el resultado del scaneo de un QR"""
    qr_code = get_object_or_404(QRCode, id=qr_id)
    return render(request, 'scanner/scan_result.html', {'qr_code': qr_code})

@api_view(['POST'])
def process_qr_scan(request):
    """API para procesar el contenido de un QR scaneo"""
    # Obtener datos del request
    data = request.data
    
    # Verificar si el contenido del QR existe
    if 'content' not in data:
        return Response({'error': 'No se proporcionó contenido QR'}, status=400)
    
    # Buscar o crear un QR Code basado en el contenido
    qr_code, created = QRCode.objects.get_or_create(content=data['content'])
    
    # Registrar el scaneo
    scan = QRScan(
        qr_code=qr_code,
        user_agent=request.META.get('HTTP_USER_AGENT', ''),
        ip_address=request.META.get('REMOTE_ADDR')
    )
    scan.save()
    
    # Devolver los datos del QR y la redirección
    return Response({
        'qr_code': QRCodeSerializer(qr_code).data,
        'redirect_url': f'/scan-result/{qr_code.id}/'
    })