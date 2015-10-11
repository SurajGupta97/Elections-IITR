from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
	user=models.OneToOneField(User)
	
	BRANCH=(
		('CS','Computer Science'),
		('EE','Electrical Engineering'),
		('ME','Mechanical Engineering'),
		('CE','Civil Engineering'),
	)
	branch= models.CharField(max_length=2,choices=BRANCH,default='CS')

	YEAR=(
		(1,'First year'),
		(2,'Second year'),
		(3,'Third year'),
		(4,'Fourth year'),
	)
	year= models.IntegerField(choices=YEAR,default=1)

	GENDER=(
		('Male','Male'),
		('Female','Female'),
	)
	gender = models.CharField(max_length=6,blank=False,choices=GENDER,default='Male')

	dob = models.DateField()

	en_no= models.IntegerField()

# Create your models here.
#Pending name
#num_votes
