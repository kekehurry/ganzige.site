from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.webhook, name='webhook'),
]
