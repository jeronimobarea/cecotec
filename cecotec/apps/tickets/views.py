# REST FRAMEWORK
from rest_framework.viewsets import ModelViewSet

# USER
from cecotec.apps.products.serializers import ProductSerializer
from cecotec.apps.tickets.models import Ticket


# Create your views here.
class TicketsViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Ticket.objects.all()

    filter_fields = {
        'client__email': ['icontains'],
    }
