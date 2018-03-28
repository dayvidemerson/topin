from rest_framework import routers

from .views import MarkerViewSet, LineViewSet, ScheduleViewSet


router = routers.SimpleRouter()
router.register('markers', MarkerViewSet)
router.register('lines', LineViewSet)
router.register('schedules', ScheduleViewSet)
urlpatterns = router.urls
