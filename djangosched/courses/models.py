from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from courses.choices import *

# possibly make more tables and use joins to make them save room and easier to access for the individual professor, room, ect. view
# Create your models here.
class Course(models.Model):
	title = models.CharField(max_length = 100)
	description = models.TextField()
	department = models.CharField(choices = DEPT_CHOICES, max_length = 30)
	level = models.CharField(choices = LEVEL_CHOICES, max_length = 20)
	First_Time_Day_Choice = models.CharField(choices = UCS_TIME_CHOICES, max_length = 10)
	Second_Time_Day_Choice = models.CharField(choices = UCS_TIME_CHOICES, max_length = 10)
	Third_Time_Day_Choice = models.CharField(choices = UCS_TIME_CHOICES, max_length = 10)
	slug = models.SlugField()
	date = models.DateTimeField(auto_now_add = True)
	professor = models.ForeignKey(User, default = None, on_delete = True)
	First_Room_Choice = models.CharField(choices = ROOM_CHOICES, max_length = 20)
	Second_Room_Choice = models.CharField(choices = ROOM_CHOICES, max_length = 20)
	Third_Room_Choice = models.CharField(choices = ROOM_CHOICES, max_length = 20)
	assigned_room = models.CharField(max_length = 20)
	assigned_time = models.CharField(max_length = 100)
	has_conflict = models.BooleanField(default = False)
	enemies = models.CharField(max_length = 3000, default = "")
	cap = models.CharField(max_length = 50)
	prerequisite = models.CharField(max_length = 300)
	term_length = models.CharField(choices = TERM_CHOICES, max_length = 30)
	LAC = models.CharField(choices = LAC_CHOICES, max_length = 10)
	Gender_Studies = models.CharField(choices = GENDER_CHOICES, max_length = 10)
	Interdisciplinary = models.CharField(choices = INTER_CHOICES, max_length = 10)

	def __str__(self):
		return self.title

	def snippet(self):
		return self.description[:50] + '...'
