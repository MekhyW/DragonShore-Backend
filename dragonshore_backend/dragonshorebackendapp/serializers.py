from rest_framework import serializers
from .models import Product, ProductMedia, Commission, CommissionStatus

class ProductMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMedia
        fields = ['id', 'file_type', 'file_url', 'thumbnail']


class ProductSerializer(serializers.ModelSerializer):
    media = ProductMediaSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'type', 'price_usd', 'price_eur', 'price_brl', 'stock_quantity', 'is_active', 'metadata', 'created_at', 'media']


class CommissionStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommissionStatus
        fields = ['id', 'status_update', 'media_url', 'timestamp']


class CommissionSerializer(serializers.ModelSerializer):
    status_updates = CommissionStatusSerializer(many=True, read_only=True)
    product_details = ProductSerializer(source='product', read_only=True)
    class Meta:
        model = Commission
        fields = ['id', 'customer_name', 'contact_email', 'product', 'product_details', 'details', 'status', 'progress_notes', 'price_estimate', 'created_at', 'status_updates']


class ProductListSerializer(serializers.ModelSerializer):
    thumbnail_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'type', 'price_usd', 'price_eur', 'price_brl', 'stock_quantity', 'is_active', 'created_at', 'thumbnail_url']
    
    def get_thumbnail_url(self, obj):
        thumbnail = obj.media.filter(thumbnail=True).first()
        if thumbnail:
            return thumbnail.file_url
        image = obj.media.filter(file_type='image').first()
        if image:
            return image.file_url
        return None


class CommissionListSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()

    class Meta:
        model = Commission
        fields = ['id', 'customer_name', 'status', 'price_estimate', 'created_at', 'product_name']

    def get_product_name(self, obj):
        if obj.product:
            return obj.product.name
        return None