from django import forms
from . import models

class CreateCourse(forms.ModelForm):
	class Meta:
		model = models.Course 
		fields = ['title', 'decription', 'slug', 'pref_day', 'pref_time', 'room']
		#will add more in depth, specific fields of different types to make it easier to 
		#input time and day options. 