from django.contrib import admin
from .models import Product, ProductMedia, Commission, CommissionStatus

admin.site.register(Product)
admin.site.register(ProductMedia)
admin.site.register(Commission)
admin.site.register(CommissionStatus)
