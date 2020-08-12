from rest_framework import serializers
from cecotec.apps.products.models import Product


# MODELS
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'created_at', 'last_modification')
