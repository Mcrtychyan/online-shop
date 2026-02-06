from django.contrib import admin
from django.urls import path, include
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # myapp - ваше приложение
] + debug_toolbar_urls()
