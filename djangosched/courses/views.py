from django.shortcuts import render, redirect
from .models import Course
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from arbiter.ucs import codes
from arbiter.sched import get_solution
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from arbiter.artime import *
from .forms import CreateCourse
from django.core.exceptions import PermissionDenied

def heiser_map(request):
	return render(request, 'courses/heisermap.html')

def ace_map(request):
	return render(request, 'courses/acemap.html')

def ready_page(request):
	if not request.user.is_superuser:
		return redirect('home:home-page')

	return render(request, 'courses/ready_page.html')

def apply_algo(request):
	if not request.user.is_superuser:
		return redirect('home:home-page')
	courses = Course.objects.all().order_by('date')
	d = {}
	for course in courses:
		d[course.id] = {'time':set([codes[course.First_Time_Day_Choice], codes[course.Second_Time_Day_Choice], codes[course.Third_Time_Day_Choice],]),
						'room':set([course.First_Room_Choice, course.Second_Room_Choice, course.Third_Room_Choice]),
						'prof':course.professor,
						'dept':course.department,
						'level':course.level,
						'name':course.title}

	solution = get_solution(d)

	if solution != 'FAILURE':
		for course_id in solution:
			course = Course.objects.get(id = course_id)
			course.assigned_room = solution[course_id]['room']
			course.assigned_time = str(solution[course_id]['time'])
			course.has_conflict = solution[course_id]['conflict']
			course.enemies = solution[course_id]['enemies']
			course.save()
		print(len(Course.objects.filter(has_conflict=True)), "conflicts")
	else:
		print('Arbiter Failed')

	return redirect('courses:list')


def translate_back(s):
	for code in codes:
		if str(codes[code]) == s:
			return codes[code]
	return TimePref([TimeSlot(WeekTime(0,0,1), WeekTime(0,0,2))])

# Create your views here.
@login_required(login_url = "/accounts/login/")
def course_list(request):
	courses = Course.objects.all()
	if request.method == "POST":
		form = forms.FilterCourseList(request.POST, request.FILES)
		if form.is_valid():
			instructor = form.cleaned_data.get('instructor')
			if instructor:
				courses = courses.filter(professor=User.objects.get(username=instructor))
			dept = form.cleaned_data.get('dept')
			if dept:
				courses = courses.filter(department=dept)
			time = form.cleaned_data.get('time')
			if time:
				courses = courses.filter(assigned_time=str(codes[time]))
			room = form.cleaned_data.get('room')
			if room:
				courses = courses.filter(assigned_room=room)
	else:
		form = forms.FilterCourseList()

	courses = sorted(courses, key=lambda course:translate_back(course.assigned_time).toord())

	return render(request, 'courses/course_list.html', {'courses':courses, 'form':form})

@login_required(login_url = "/accounts/login/")
def prof_course_list(request, prof):
	courses = Course.objects.filter(professor=User.objects.get(username=prof))
	courses = sorted(courses, key=lambda course:translate_back(course.assigned_time).toord())
	form = forms.FilterCourseList()

	return render(request, 'courses/course_list.html', {'courses':courses, 'form':form})

@login_required(login_url = "/accounts/login/")
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
			instance.slug = slugify(request.POST.get("title", ""))
			instance.save()
			return redirect('courses:list')
	else:
		form = forms.CreateCourse()
	return render(request, 'courses/course_create.html', {'form':form})

@login_required(login_url = "/accounts/login/")
def edit_course(request, slug):
	instance = Course.objects.get(slug=slug)

	if request.user != instance.professor and not request.user.is_superuser:
		return redirect('courses:detail', slug=instance.slug)

	if request.method == "POST":
		form = forms.CreateCourse(request.POST, instance=instance)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.slug = slugify(request.POST.get("title", ""))
			instance.save()
			return redirect('courses:detail', slug=instance.slug)
	else:
		form = forms.CreateCourse(instance = instance)

	context = {
		'form':form,
		'course':instance
	}
	return render(request, 'courses/edit_course.html', context)

@login_required(login_url = "/accounts/login/")
def course_delete(request, slug):
	instance = Course.objects.get(slug=slug)

	if request.user != instance.professor and not request.user.is_superuser:
		return redirect('courses:detail', slug=instance.slug)

	if request.user == instance.professor:
		instance.delete()
		return redirect('courses:list')
	else:
		return redirect('courses:detail', slug=instance.slug)
