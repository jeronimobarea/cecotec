from django.conf.urls import url, include
from rest_framework import routers
from cecotec.apps.tickets import views

# Register API Endpoints
router = routers.SimpleRouter()
router.register('tickets', views.TicketsViewSet, basename='tickets')

urlpatterns = [
    url(r'^', include(router.urls)),
]
