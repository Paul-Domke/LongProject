from django import forms
from . import models
from courses.choices import *

class CreateCourse(forms.ModelForm):
	class Meta:
		model = models.Course
		fields = ['title', 'department', 'level', 'decription', 'slug', 'ucs_time_date1', 'ucs_time_date2', 'ucs_time_date3', 'room1', 'room2', 'room3']
		#will add more in depth, specific fields of different types to make it easier to
		#input time and day options.

class FilterCourseList(forms.Form):
	instructor = forms.ModelChoiceField(label='Instructor:', queryset=models.User.objects.all().order_by('username'), required=False)
	time = forms.ChoiceField(label='Time:', choices=UCS_TIME_CHOICES, required=False)
