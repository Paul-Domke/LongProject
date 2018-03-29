from django.db import models
from django.contrib.auth.models import User
from courses.choices import *


# Create your models here.
class Course(models.Model):
	title = models.CharField(max_length = 100)
	decription = models.TextField()
	ucs_time_date = models.CharField(choices = UCS_TIME_CHOICES, max_length = 10)
	slug = models.SlugField()
	date = models.DateTimeField(auto_now_add = True)
	professor = models.ForeignKey(User, default = None, on_delete = True)
	room = models.CharField(max_length = 10)

	def __str__(self):
		return self.title

	def snippet(self):
		return self.decription[:50] + '...'
