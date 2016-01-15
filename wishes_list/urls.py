"""wishes_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import url, patterns, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers
from core.viewsets import ContactViewSet
from users.viewsets import *
from wishes.viewsets import *
from products.viewsets import *
from . import settings
admin.site.site_header = settings.ADMIN_SITE_HEADER

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'friendship', FrendshipViewSet)
router.register(r'event', EventViewSet)
router.register(r'gifts', GiftViewSet)
router.register(r'ivited_friends', EventInvitedViewSet)
router.register(r'shops', ShopViewSet)
router.register(r'product', ProductViewSet)
router.register(r'contact', ContactViewSet, base_name='contact')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls, namespace='api')),
    url(r'^', include("core.urls", namespace='core')),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api/auth$', AuthView.as_view(), name='authenticate')
]




if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))