from django.conf.urls import include, url
from .import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^page_(?P<page>[0-9]+)/$', views.index, name='page'),
    url(r'^page_(?P<page>[0-9]+)/blog_(?P<blog_id>[0-9]+)/(?P<capture_id>[0-9]+)/$',
        views.detail, name='detail'),
    url(r'^author_(?P<author_id>[0-9]+)/$', views.author, name='author'),
    url(r'^author_(?P<author_id>[0-9]+)/(?P<page>[0-9]+)/$',
        views.author, name='author_page'),
    url(r'^tag_(?P<tag_id>[0-9]+)/$', views.tag, name='tag'),
    url(r'^tag_(?P<tag_id>[0-9]+)/(?P<page>[0-9]+)/$',
        views.tag, name='tag_page'),

]
