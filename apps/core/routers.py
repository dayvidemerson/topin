from rest_framework import routers

from .views import StateViewSet, CityViewSet


router = routers.SimpleRouter()
router.register('states', StateViewSet)
router.register('cities', CityViewSet)
urlpatterns = router.urls
