from django.urls import path
from xpressbus.views import index
from .views import RouteStopView, RoutePredictView
from xpressbus import views

urlpatterns = [
    path("", index, name="index"),
    path("getPredict", RoutePredictView.as_view(), name="get_predict_info"),
    path("getinfo/", RouteStopView.as_view(), name="get_stops_info"),
    path("getinfo/<int:id>", views.stop_detail, name="get_detail_per_stop"),
    path("getRealTime/<int:busNo>", views.realTimeData, name="realTimeData"),
]
