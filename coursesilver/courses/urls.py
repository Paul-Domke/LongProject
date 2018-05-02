from django.conf.urls import url
from django.urls import include, path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'courses'

urlpatterns = [
    url(r'^$', views.course_list, name = 'list'),
    url(r'^(?P<slug>[\w-]+)/edit/$', views.edit_course, name = 'edit_course'),
    url(r'^create/$', views.course_create, name = 'create'),
    path('user/<prof>/', views.prof_course_list, name = 'prof'),
    url(r'^(?P<slug>[\w-]+)/$', views.course_details, name = 'detail'),
    url(r'^apply_algo$', views.apply_algo, name = 'apply_algo'),
]

urlpatterns += staticfiles_urlpatterns()
