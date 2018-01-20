from django.conf.urls import include, url
from .import views

urlpatterns = [
    url(r'^aria2/$', views.aria2, name='aria2'),]
