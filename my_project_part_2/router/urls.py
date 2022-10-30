# TODO опишите здесь маршрутизацию с помощью класса SimpleRouter
from rest_framework import routers

from router import views

router_set = routers.SimpleRouter()
router_set.register("router_stores", views.StoreViewSet)

urlpatterns = []

urlpatterns += router_set.urls
