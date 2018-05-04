from django import forms
from . import models
from courses.choices import *

class CreateCourse(forms.ModelForm):
	class Meta:
		model = models.Course
		fields = ['title', 'department', 'level', 'decription', 'ucs_time_date1', 'ucs_time_date2', 'ucs_time_date3', 'room1', 'room2', 'room3', 'cap', 'term_length', 'prerequisite', 'LAC', 'Gender_Studies', 'Interdisciplinary']

		labels = {'decription':'Description',
				  'ucs_time_date1':'First Choice Time',
				  'ucs_time_date2':'Second Choice Time',
				  'ucs_time_date3':'Third Choice Time',
				  'room1':'First Choice Room',
				  'room2':'Second Choice Room',
				  'room3':'Third Choice Room',
				  'cap':'Max Number of Students',
				  }
		#will add more in depth, specific fields of different types to make it easier to
		#input time and day options.





class FilterCourseList(forms.Form):
	instructor = forms.ModelChoiceField(label='Instructor:', queryset=models.User.objects.all().order_by('username'), required=False)
	dept = forms.ChoiceField(label='Department:', choices=DEPT_CHOICES, required=False)
	time = forms.ChoiceField(label='Time:', choices=UCS_TIME_CHOICES, required=False)
	room = forms.ChoiceField(label='Location:', choices=ROOM_CHOICES, required=False)
