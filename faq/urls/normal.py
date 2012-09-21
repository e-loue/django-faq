from django.conf.urls.defaults import *

from faq.views.shallow import TopicList
from faq.views.normal import TopicDetail, question_detail


# Include these patterns if you want URLs like:
#
#   /faq/
#   /faq/topic/
#   /faq/topic/#question
#

urlpatterns = patterns('',
    url(r'^$', TopicList.as_view(), name='faq-topic-list'),
    url(r'^(?P<slug>[-\w]+)/$', TopicDetail.as_view(), name='faq-topic-detail'),
    url(r'^(?P<topic_slug>[-\w]+)/(?P<slug>[-\w]+)/$', question_detail,
        name='faq-question-detail'),
)
