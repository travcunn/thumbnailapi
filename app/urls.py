from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import thumbnailapi.views


urlpatterns = [
    url(r'^$', thumbnailapi.views.index, name='index'),
    path('convert/image/', thumbnailapi.views.convert_image),
    path('admin/', admin.site.urls),
]
