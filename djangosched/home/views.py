from django.shortcuts import render
from courses.models import Course
from courses.forms import forms

# Create your views here.
def home_view(request):
	courses = Course.objects.all().order_by('date')
	return render(request, 'home/home_page.html', {'courses':courses})
	