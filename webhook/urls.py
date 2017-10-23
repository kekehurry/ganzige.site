from django.conf.urls import url
from webhook import views

urlpatterns = [
    url(r'^$', views.webhook, name='webhook'),
]
