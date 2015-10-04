from django.shortcuts import render
from .models import Votes
from django.http import HttpResponseRedirect

def index(request):
	return render(request, 'voting/index.html')

def details(request , vote_id):
	if request.method=="GET":
		#application logic to get the standing position and the avaiable candidates
		#default
		position = "General Secretary UG Academics"
		candidates = ["Punit Dhoot" , "Suraj Gupta" , "Jhatu Shah" , "Personality Wala"]
		context = {'position' : position , 'candidates': candidates}
		print Votes.objects.get(user_id =1).vote1
		return render(request , 'voting/vote.html' , context)
	elif request.method=="POST":
		column = 'vote' + `int(vote_id)`
		print column
		try:
			candidate_voted = int(request.POST['vote'])
			vote = Votes(user_id=candidate_voted)
			setattr(vote , column, True)
			vote.save()
			return HttpResponseRedirect('/vote/2')
		except:
			pass
