from django.shortcuts import render, redirect
from .models import Course
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from arbiter.ucs import codes
from arbiter.sched import get_solution
from django.contrib.auth.models import User

def apply_algo(request):
	courses = Course.objects.all().order_by('date')
	d = {}
	for course in courses:
		d[course.id] = {'time':[codes[course.ucs_time_date1], codes[course.ucs_time_date2], codes[course.ucs_time_date3],],
						'room':[course.room1, course.room2, course.room3],
						'prof':course.professor,
						'dept':course.department,
						'level':course.level}

	solution = get_solution(d)

	for course_id in solution:
		course = Course.objects.get(id = course_id)
		course.assigned_room = solution[course_id]['room']
		course.assigned_time = str(solution[course_id]['time'])
		course.save()

		return render(request, 'home/home_page.html', {'courses':courses})


# Create your views here.
def course_list(request):
	courses = Course.objects.all().order_by('date')
	if request.method == "POST":
		form = forms.FilterCourseList(request.POST, request.FILES)
		if form.is_valid():
			if form.cleaned_data.get('instructor'):
				courses = courses.filter(professor=User.objects.get(username=form.cleaned_data.get('instructor')))
			if form.cleaned_data.get('dept'):
				courses = courses.filter(department=form.cleaned_data.get('dept'))
			if form.cleaned_data.get('time'):
				courses = courses.filter(assigned_time=str(codes[form.cleaned_data.get('time')]))
			if form.cleaned_data.get('room'):
				courses = courses.filter(assigned_room=form.cleaned_data.get('room'))
	else:
		form = forms.FilterCourseList()


	return render(request, 'courses/course_list.html', {'courses':courses, 'form':form})

def prof_course_list(request, prof):
	courses = Course.objects.filter(professor=User.objects.get(username=prof)).order_by('date')

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
