from django.db import models

class Output(models.Model):
	course_id = models.CharField(max_length = 10)
	assigned_time = models.CharField(max_length = 15)
	assigned_room =  models.CharField(max_length = 20)
	