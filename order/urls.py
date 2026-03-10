from django.urls import path,include
from rest_framework import routers

from order.viewsets import *

router = routers.SimpleRouter()
router.register(r'order', viewsets.OrderViewSet, basename='order')


urlpatterns = [
    path('', include(router.urls)),
]

