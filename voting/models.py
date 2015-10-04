from django.db import models
from django.contrib.auth.models import User

class Votes(models.Model):
	user = models.OneToOneField(User)
	vote1 = models.BooleanField(default = False)
	vote2 = models.BooleanField(default = False)
	vote3 = models.BooleanField(default = False)
	vote4 = models.BooleanField(default = False)

class Positions(models.Model):
	position = models.CharField(max_length = 100)