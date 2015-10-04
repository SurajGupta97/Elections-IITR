from django.shortcuts import render
from .models import Votes

def index(request):
	return render(request, 'voting/index.html')

def details(request , vote_id):
	if request.method=="GET":
		#application logic to get the standing position and the avaiable candidates
		#default
		position = "General Secretary UG Academics"
		candidates = ["Punit Dhoot" , "Suraj Gupta" , "Jhatu Shah" , "Personality Wala"]
		context = {'position' : position , 'candidates': candidates}
		return render(request , 'voting/vote.html' , context)
	elif request.method=="POST":
		