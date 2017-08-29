from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="events"),
    url(r'^(?P<id>\d+)/$', views.event, name="eventpost"),
    url(r'^shifts/(?P<id>\d+)/$', views.shift, name="shift"),
]