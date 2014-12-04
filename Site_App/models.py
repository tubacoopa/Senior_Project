from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
	username = models.CharField(max_length=400)
	title = models.CharField(max_length=400)
	zipcode = models.CharField(max_length=5)
	description = models.CharField(max_length=400)
	
class Join(models.Model):
	username = models.CharField(max_length=400)
	title = models.CharField(max_length=400)