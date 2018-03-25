from django.db import models

class Login(models.Model):
	email = models.CharField(max_length = 60)
	password = models.CharField(max_length = 15)
	def __str__(self):
		return self.email