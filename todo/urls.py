from rest_framework import routers
from .api import *

router = routers.DefaultRouter()
router.register('api/todo', TodoViewSet, 'todo')

urlpatterns = router.urls
