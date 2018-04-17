from django.conf.urls import url
from django.urls import include, path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'courses'

urlpatterns = [
    url(r'^$', views.course_list, name = 'list'),
    url(r'^create/$', views.course_create, name = 'create'),
<<<<<<< HEAD
    path('user/<prof>/', views.prof_course_list, name = 'prof'),
=======
    path('prof/<prof>/', views.prof_course_list, name = 'prof'),
>>>>>>> be06c59ed1407d296dcae7dd22b72e0d2fc33c7b
    url(r'^(?P<slug>[\w-]+)/$', views.course_details, name = "detail"),
]

urlpatterns += staticfiles_urlpatterns()
