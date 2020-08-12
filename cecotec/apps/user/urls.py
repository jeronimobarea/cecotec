from django.conf.urls import url, include
from rest_framework import routers
from cecotec.apps.user import views

# Register API Endpoints
router = routers.SimpleRouter()
router.register('user', views.UserViewSet, basename='user')

urlpatterns = [
    url(r'^', include(router.urls)),
]
