from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from courses import views as course_views
from home import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home_view, name = "home"),
    path('about/', views.about),
    path('courses/', include('courses.urls')),
    path('accounts/', include('accounts.urls')),
]

urlpatterns += staticfiles_urlpatterns()