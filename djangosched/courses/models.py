from django.db import models
from django.contrib.auth.models import User
from courses.choices import *


# Create your models here.
class Course(models.Model):
	title = models.CharField(max_length = 100)
	decription = models.TextField()
	ucs_time_date1 = models.CharField(choices = UCS_TIME_CHOICES, max_length = 10)
	ucs_time_date2 = models.CharField(choices = UCS_TIME_CHOICES, max_length = 10)
	ucs_time_date3 = models.CharField(choices = UCS_TIME_CHOICES, max_length = 10)
	slug = models.SlugField()
	date = models.DateTimeField(auto_now_add = True)
	professor = models.ForeignKey(User, default = None, on_delete = True)
	room1 = models.CharField(choices = ROOM_CHOICES, max_length = 20)
	room2 = models.CharField(choices = ROOM_CHOICES, max_length = 20)
	room3 = models.CharField(choices = ROOM_CHOICES, max_length = 20)

	def __str__(self):
		return self.title

	def snippet(self):
		return self.decription[:50] + '...'
