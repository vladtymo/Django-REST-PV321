from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework import routers

from products import views
from products.views import ProductList
from rest_framework.schemas import get_schema_view
from rest_framework.renderers import JSONOpenAPIRenderer

router = routers.SimpleRouter()
# router.register(r'products', views.ProductList, basename='product')

schema_view = get_schema_view(
    title="Server Monitoring API",
    url="https://www.example.org/api/",
    renderer_classes=[JSONOpenAPIRenderer],
)

urlpatterns = [
    path("schema.json", schema_view),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
    path('api/', include('products.urls')),
]

urlpatterns += router.urls


