# REST FRAMEWORK
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# USER
from cecotec.apps.user.serializers import BasicUserSerializer
from cecotec.apps.user.models import User


# Create your views here.
class UserViewSet(ModelViewSet):
    serializer_class = BasicUserSerializer
    queryset = User.objects.all()

    @action(detail=False, methods=['get'])
    def me(self, request):
        return Response(BasicUserSerializer(self.request.user).data)
