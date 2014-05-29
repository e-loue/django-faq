# -*- coding: utf-8 -*-

# Django 1.6 fix
try:
    from django.conf.urls import *
except ImportError:
    from django.conf.urls.defaults import *

from faq.views.shallow import topic_list
from faq.views.normal import topic_detail
from faq.views.deep import QuestionDetail


# Include these patterns if you want URLs like:
#
#   /faq/
#   /faq/topic/
#   /faq/topic/question/
#

urlpatterns = patterns('',
    url(r'^$', topic_list, name='faq-topic-list'),
    url(r'^(?P<slug>[-\w]+)/$', topic_detail, name='faq-topic-detail'),
    url(r'^(?P<topic_slug>[-\w]+)/(?P<slug>[-\w]+)/$', QuestionDetail.as_view(),
        name='faq-question-detail'),
)
