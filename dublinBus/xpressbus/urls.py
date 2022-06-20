from django.urls import path
from xpressbus.views import index

urlpatterns = {
    path("", index, name="index"),
}
