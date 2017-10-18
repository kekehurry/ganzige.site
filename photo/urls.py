from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^page_(?P<page>[0-9]+)/$', views.index, name='page'),
    url(r'^image_(?P<image_id>[0-9]+)/$', views.detail, name='detail')
]
