# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from unach_photo.urls import urlpatterns as unach_photo_urls

urlpatterns = [
    url(r'^', include(unach_photo_urls, namespace='unach_photo')),
]
