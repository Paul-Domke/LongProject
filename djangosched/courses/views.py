from django.shortcuts import render, redirect
from .models import Course
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from .ucs import codes
from .sched import *


# Create your views here.
def course_list(request):
	courses = Course.objects.all().order_by('date')
	# TODO: move this stuff
	# from here to next comment can be moved somewhere else and needs to be called when a new course is submitted
	# courses = Course.objects.all().order_by('date')
	d = {}
	for course in courses:
		d[course.id] = {'time':[codes[course.ucs_time_date1], codes[course.ucs_time_date2], codes[course.ucs_time_date3],],
						'room':[course.room1, course.room2, course.room3],
						'prof':course.professor}
	solution = get_solution(d)
	
	for course_id in solution:
		course = Course.objects.get(id = course_id)
		course.assigned_room = solution[course_id]['room']
		course.assigned_time = str(solution[course_id]['time'])
		course.save()
	# end of stuff to move
		
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