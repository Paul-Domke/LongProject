from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'courses'

urlpatterns = [
    url(r'^$', views.course_list, name = 'list'),
    url(r'^create/$', views.course_create, name = 'create'),
    url(r'^(?P<slug>[\w-]+)/$', views.course_details, name = 'detail'),
]

urlpatterns += staticfiles_urlpatterns()