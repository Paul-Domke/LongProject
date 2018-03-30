from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'home'

urlpatterns = [
    url(r'^$', views.home_view, name = 'home-page'),
    ]

urlpatterns += staticfiles_urlpatterns()