# Django 1.6 fix
try:
    from django.conf.urls import *
except ImportError:
    from django.conf.urls.defaults import *


urlpatterns = patterns('',
    (r'^faq/', include('faq.urls')),
)
