from django.db import models

class Input(models.Model):
	course_id = models.CharField(max_length = 10)
	professor_id = models.CharField(max_length = 10)
	room_pref = models.CharField(max_length = 500)
	time_pref = models.CharField(max_length = 15)
	class_size = models.CharField(max_length = 3)
	audio_visual = models.CharField(max_length = 1)
	projector = models.CharField(max_length = 1)
	tvs =  models.CharField(max_length = 1)
	black_board = models.CharField(max_length = 1)
	white_board = models.CharField(max_length = 1)
	stadium = models.CharField(max_length = 1)
	computer_lab = models.CharField(max_length = 1)
	lab = models.CharField(max_length = 1)
	conference_room = models.CharField(max_length = 1)
	outlets = models.CharField(max_length = 1)
	# time_stamp = models.DateTimeField(default = time_stamp)