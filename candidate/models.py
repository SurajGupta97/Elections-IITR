from django.db import models
from django.contrib.auth.models import User
import os

class Candidate(models.Model):
	user = models.OneToOneField(User)
	post = models.IntegerField(null = False)
	votes = models.IntegerField(default = 0)
	user_dir = 1
	if not os.path.exists(user_dir):
		os.makedirs(user_dir)
	manifesto = models.FileField(upload_to = user_dir)
	image = models.ImageField(upload_to = user_dir)