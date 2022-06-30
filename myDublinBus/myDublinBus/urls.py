"""myDublinBus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
<<<<<<< HEAD:dublinBus/dublinBus/urls.py
from django.urls import path, include
=======
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

<<<<<<< HEAD
>>>>>>> 7a0517c744007e9998f720044138a9fdea369890:myDublinBus/myDublinBus/urls.py
=======
>>>>>>> 7704d1cdf6da33d631aa6428db85189164dc1004

urlpatterns = [
    path('', include('xpressbus.urls')),
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
      

]
