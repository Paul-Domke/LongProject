from django.shortcuts import render
from courses.models import Course
from courses.forms import forms
from courses.views import translate_back
from arbiter.artime import TimePref

# Create your views here.
def home_view(request):
	courses = Course.objects.all().order_by('date')
	courses = sorted(courses, key=lambda course:translate_back(course.assigned_time).toord())
	return render(request, 'home/home_page.html', {'courses':courses})
