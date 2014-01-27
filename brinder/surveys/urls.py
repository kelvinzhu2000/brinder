from django.conf.urls import patterns,url

from surveys import views

urlpatterns = patterns('',
    url(r'^(?P<message_url>\w+)$', views.survey, name='survey'),
)
