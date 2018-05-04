from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from courses.choices import *
from django.core.validators import MaxValueValidator

# possibly make more tables and use joins to make them save room and easier to access for the individual professor, room, ect. view
# Create your models here.
class Course(models.Model):
	title = models.CharField(max_length = 100)
	decription = models.TextField()
	department = models.CharField(choices = DEPT_CHOICES, max_length = 30)
	level = models.CharField(choices = LEVEL_CHOICES, max_length = 20)
	ucs_time_date1 = models.CharField(choices = UCS_TIME_CHOICES, max_length = 10)
	ucs_time_date2 = models.CharField(choices = UCS_TIME_CHOICES, max_length = 10)
	ucs_time_date3 = models.CharField(choices = UCS_TIME_CHOICES, max_length = 10)
	slug = models.SlugField()
	date = models.DateTimeField(auto_now_add = True)
	professor = models.ForeignKey(User, default = None, on_delete = True)
	room1 = models.CharField(choices = ROOM_CHOICES, max_length = 20)
	room2 = models.CharField(choices = ROOM_CHOICES, max_length = 20)
	room3 = models.CharField(choices = ROOM_CHOICES, max_length = 20)
	assigned_room = models.CharField(max_length = 20)
	assigned_time = models.CharField(max_length = 100)
	has_conflict = models.BooleanField(default = False)
	enemies = models.CharField(max_length = 3000, default = "")
	cap = models.IntegerField(default = 0, validators=[MaxValueValidator(85)])
	prerequisite = models.CharField(max_length = 300, blank=True)
	term_length = models.CharField(choices = TERM_CHOICES, max_length = 30)
	LAC = models.BooleanField(default = False)
	Gender_Studies = models.BooleanField(default = False)
	Interdisciplinary = models.BooleanField(default = False)

	def __str__(self):
		return self.title

	def snippet(self):
		return self.decription[:50] + '...'
