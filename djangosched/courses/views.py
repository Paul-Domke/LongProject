from django.shortcuts import render, redirect
from .models import Course
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

def course_list(request):
	courses = Course.objects.all().order_by('date')
	# I think that this is where the algorithm will go into place
	
	return render(request, 'courses/course_list.html', {'courses':courses})

def course_details(request, slug):
	# return HttpResponse("This is where the description will be")
	course = Course.objects.get(slug = slug)
	return render(request, 'courses/course_detail.html', {'course':course})

@login_required(login_url="/accounts/login/")
def course_create(request):
	if request.method == "POST":
		form = forms.CreateCourse(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.professor = request.user
			instance.save()
			return redirect('courses:list')
	else:
		form = forms.CreateCourse()
	return render(request, 'courses/course_create.html', {'form':form})