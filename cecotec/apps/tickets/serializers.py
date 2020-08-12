from rest_framework import serializers

from cecotec.apps.products.serializers import ProductSerializer
from cecotec.apps.tickets.models import ProductsInTicket, Ticket


class ProductsInTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsInTicket
        fields = ('id', 'ticket', 'product')


class TicketSerializer(serializers.ModelSerializer):
    products = ProductSerializer()

    class Meta:
        model = Ticket
        fields = ('id', 'client', 'products', 'created_at', 'last_modification')
