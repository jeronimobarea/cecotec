from django.conf.urls import url, include
from rest_framework import routers
from cecotec.apps.products import views

# Register API Endpoints
router = routers.SimpleRouter()
router.register('products', views.ProductsViewSet, basename='products')

urlpatterns = [
    url(r'^', include(router.urls)),
]
