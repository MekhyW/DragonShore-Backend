from django.urls import path
from django.contrib import admin
from . import views

admin.site.site_header = 'DragonShore Administration'
admin.site.index_title = 'Database'
admin.site.site_title = 'DragonShore Administration'

urlpatterns = [
    path("", views.index, name="index"),
]