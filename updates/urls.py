from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="updates"),
    url(r'^(?P<id>\d+)/$', views.post, name="updatepost"),
]