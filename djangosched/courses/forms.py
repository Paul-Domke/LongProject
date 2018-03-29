from django import forms
from . import models
from courses.choices import *

class CreateCourse(forms.ModelForm):
	ucs_time_date = forms.ChoiceField(choices = UCS_TIME_CHOICES, required = True)
	class Meta:
		model = models.Course 		
		fields = ['title', 'decription', 'slug', 'room']
		#will add more in depth, specific fields of different types to make it easier to 
		#input time and day options. 