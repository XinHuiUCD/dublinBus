from django.urls import path 
from . import views
from django.conf.urls import include

# from .views import CustomLoginView

# app_name = "home"

urlpatterns = [

    # path('login/', CustomLoginView.as_view(), name='login'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path("register/", views.register_request, name="register"),
    path("twitter/", views.twitter, name="twitter"),




]