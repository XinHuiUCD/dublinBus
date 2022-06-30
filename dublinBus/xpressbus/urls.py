from django.urls import path, include
from xpressbus.views import index
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)


urlpatterns = [
    path("", index, name="index"),
    path("hero/", include(router.urls)),
    path("api-auth/", include('rest_framework.urls', namespace='rest_framework'))
]
