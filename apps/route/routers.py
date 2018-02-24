from rest_framework import routers

from .views import MarkerViewSet, LineViewSet, ScheduleViewSet, RouteViewSet


router = routers.SimpleRouter()
router.register('markers', MarkerViewSet)
router.register('lines', LineViewSet)
router.register('schedules', ScheduleViewSet)
router.register('routes', RouteViewSet)
urlpatterns = router.urls
