from api.viewsets import RestaurantViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('restaurants',RestaurantViewset)
