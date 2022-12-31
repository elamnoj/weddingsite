from django.urls import re_path, path
from django.conf import settings

from . import views

from django.contrib.sitemaps.views import sitemap



urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
    #  name='django.contrib.sitemaps.views.sitemap')
]
