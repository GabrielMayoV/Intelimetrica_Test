from rest_framework import viewsets
from . import models
from . import serializers

class RestaurantViewset(viewsets.ModelViewSet):
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer
