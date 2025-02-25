from django.db import models
from django.contrib.postgres.fields import JSONField

class Product(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ('premade', 'Premade'),
        ('customizable', 'Customizable'),
        ('commission', 'Commission-Based'),
    ]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=PRODUCT_TYPE_CHOICES)
    price_usd = models.DecimalField(max_digits=10, decimal_places=2)
    price_eur = models.DecimalField(max_digits=10, decimal_places=2)
    price_brl = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    metadata = JSONField(blank=True, null=True)  # Flexible fields (e.g., size, color)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class ProductMedia(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('image', 'Image'),
        ('3d_model', '3D Model'),
        ('video', 'Video'),
    ]
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, related_name='media', on_delete=models.CASCADE)
    file_type = models.CharField(max_length=20, choices=MEDIA_TYPE_CHOICES)
    file_url = models.URLField()
    thumbnail = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.product.name} - {self.file_type}"


class Commission(models.Model):
    COMMISSION_STATUS_CHOICES = [
        ('queued', 'Queued'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    product = models.ForeignKey(Product, related_name='commissions', on_delete=models.SET_NULL, null=True, blank=True)
    details = JSONField(blank=True, null=True)  # Customization details, refs
    status = models.CharField(max_length=20, choices=COMMISSION_STATUS_CHOICES, default='queued')
    progress_notes = models.TextField(blank=True, null=True)
    price_estimate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Commission by {self.customer_name} - {self.status}"


class CommissionStatus(models.Model):
    id = models.AutoField(primary_key=True)
    commission = models.ForeignKey(Commission, related_name='status_updates', on_delete=models.CASCADE)
    status_update = models.CharField(max_length=255)
    media_url = models.URLField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.commission.customer_name} - {self.status_update}"
