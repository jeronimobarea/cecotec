# REST FRAMEWORK
from rest_framework.viewsets import ModelViewSet

# USER
from cecotec.apps.products.serializers import ProductSerializer
from cecotec.apps.products.models import Product


# Create your views here.
class ProductsViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    filter_fields = {
        'name': ['icontains'],
    }

    ordering_fields = ['price', ]
