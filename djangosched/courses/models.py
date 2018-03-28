from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
	title = models.CharField(max_length = 100)
	pref_time = models.CharField(max_length = 10)
	decription = models.TextField()
	slug = models.SlugField()
	date = models.DateTimeField(auto_now_add = True)
	pref_day = models.CharField(max_length = 20)
	professor = models.ForeignKey(User, default = None, on_delete = True)
	room = models.CharField(max_length = 10)

	def __str__(self):
		return self.title

	def snippet(self):
		return self.decription[:50] + '...'
