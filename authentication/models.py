from django.db import models

class User(models.Model):
	user_name= models.CharField(max_length=100)

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

	en_no= models.IntegerField()

	post= models.IntegerField()

# Create your models here.
