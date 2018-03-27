from django import forms
from . import models

class CreateCourse(forms.ModelForm):
	class Meta:
		model = models.Course 
		fields = ['title', 'decription', 'slug', 'pref_day', 'pref_time', 'room']