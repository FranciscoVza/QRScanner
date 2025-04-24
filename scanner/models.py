from django.db import models
import uuid
from django.utils.timezone import now
from simple_history.models import HistoricalRecords  # Para auditoría

class Category(models.Model):
    """Categorías para clasificar los productos."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    """Productos que se gestionan en el inventario."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    qr_code = models.OneToOneField('QRCode', on_delete=models.CASCADE, related_name='product', null=True, blank=True)
    history = HistoricalRecords()  # Auditoría de cambios

    def __str__(self):
        return self.name

class InventoryMovement(models.Model):
    """Historial de movimientos de inventario."""
    MOVEMENT_TYPES = [
        ('IN', 'Entrada'),
        ('OUT', 'Salida'),
        ('ADJ', 'Ajuste'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='movements')
    movement_type = models.CharField(max_length=3, choices=MOVEMENT_TYPES)
    quantity = models.IntegerField()  # Puede ser positivo o negativo
    timestamp = models.DateTimeField(default=now)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_movement_type_display()} - {self.quantity} - {self.product.name}"

class QRCode(models.Model):
    """Códigos QR asociados a productos."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"QR: {self.content[:30]}{'...' if len(self.content) > 30 else ''}"

class QRScan(models.Model):
    """Registro de escaneos de códigos QR."""
    qr_code = models.ForeignKey(QRCode, on_delete=models.CASCADE, related_name='scans')
    scanned_at = models.DateTimeField(auto_now_add=True)
    user_agent = models.TextField(blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)

    def __str__(self):
        return f"Scan: {self.qr_code} at {self.scanned_at}"