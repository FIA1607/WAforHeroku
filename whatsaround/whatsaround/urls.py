"""whatsaround URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include, re_path

from whatsaroundapp.views import *
from rest_framework import routers

from . import settings
from .yasg import urlpatterns as doc_urls

router = routers.SimpleRouter()
router.register(r'users', OwnUserViewSet)
router.register(r'points', PointViewSet, basename='points')
router.register(r'guests', GuestViewSet)
router.register(r'tags', TagViewSet)
router.register(r'photos', PhotoViewSet)
router.register(r'pointmessages', PointMessageViewSet)
router.register(r'usermessages', UserMessageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/drf-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += doc_urls
