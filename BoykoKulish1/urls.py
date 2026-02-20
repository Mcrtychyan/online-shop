from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import include, path

from myapp.views import ProductDetailView


class ProductsDetailView:
    @classmethod
    def as_view(cls):
        pass


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('myapp.urls')),
                  # path('cart/', include('cart.urls')),
                  path('cart/', include('cart.urls')),
path('products/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),

              ] + debug_toolbar_urls()
