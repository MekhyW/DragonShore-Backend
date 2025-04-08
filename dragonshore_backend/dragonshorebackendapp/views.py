from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from .models import Product, ProductMedia, Commission, CommissionStatus
from .serializers import (ProductSerializer, ProductMediaSerializer, CommissionSerializer, CommissionStatusSerializer, ProductListSerializer, CommissionListSerializer)

def index(request):
    return HttpResponse("Yarr! This be the Dragonshore backend app.")

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset for viewing products.
    """
    queryset = Product.objects.filter(is_active=True)
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['type']
    search_fields = ['name', 'description']
    ordering_fields = ['price_usd', 'created_at', 'name']
    ordering = ['name']
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return ProductSerializer
    
    @action(detail=False, methods=['get'])
    def premade(self, request):
        premade = Product.objects.filter(type='premade', is_active=True)
        serializer = ProductListSerializer(premade, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def customizable(self, request):
        customizable = Product.objects.filter(type='customizable', is_active=True)
        serializer = ProductListSerializer(customizable, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def commission_based(self, request):
        commission_based = Product.objects.filter(type='commission', is_active=True)
        serializer = ProductListSerializer(commission_based, many=True)
        return Response(serializer.data)


class ProductMediaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset for viewing product media.
    """
    queryset = ProductMedia.objects.all()
    serializer_class = ProductMediaSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product', 'file_type', 'thumbnail']


class CommissionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset for viewing commissions.
    """
    queryset = Commission.objects.all()
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['status', 'product']
    ordering_fields = ['created_at', 'status']
    ordering = ['-created_at']
    
    def get_serializer_class(self):
        if self.action == 'list':
            return CommissionListSerializer
        return CommissionSerializer
    
    @action(detail=False, methods=['get'])
    def by_status(self, request, status):
        commissions = Commission.objects.filter(status=status)
        serializer = CommissionListSerializer(commissions, many=True)
        return Response(serializer.data)


class CommissionStatusViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset for viewing commission status updates.
    """
    queryset = CommissionStatus.objects.all()
    serializer_class = CommissionStatusSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['commission']
    ordering_fields = ['timestamp']
    ordering = ['-timestamp']
