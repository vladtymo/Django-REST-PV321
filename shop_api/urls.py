from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

from products import views
from products.views import ProductList

# router = routers.SimpleRouter()
# router.register(r'products', views.ProductList, basename='product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
]

