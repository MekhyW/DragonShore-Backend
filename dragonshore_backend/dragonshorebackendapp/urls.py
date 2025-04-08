from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from . import views

admin.site.site_header = 'DragonShore Administration'
admin.site.index_title = 'Database'
admin.site.site_title = 'DragonShore Administration'

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'product-media', views.ProductMediaViewSet)
router.register(r'commissions', views.CommissionViewSet)
router.register(r'commission-status', views.CommissionStatusViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path('api/', include(router.urls)),
    path('api/commissions/status/<str:status>/', views.CommissionViewSet.as_view({'get': 'by_status'})),
]