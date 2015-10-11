from django.shortcuts import render
from .models import Votes, Positions
from authentication.models import User
from django.http import HttpResponseRedirect
from candidate.models import Candidate

def index(request):
	return render(request, 'voting/index.html')

def details(request , vote_id):
	if request.method=="GET":
		#application logic to get the standing position and the avaiable candidates
		#default
		position = Positions.objects.get(pk=int(vote_id)).position
		candidates = User.objects.all().filter(post=int(vote_id))
		context = {'position' : position , 'candidates': candidates}
		return render(request , 'voting/vote.html' , context)
	elif request.method=="POST":
		column = 'vote' + str(vote_id)
		print(column)
		try:
			candidate_voted = int(request.POST['vote'])
			try:
				vote = Votes.objects.get(user_id = candidate_voted)
				setattr(vote, column , True)
				vote.save()
			except:
				vote = Votes(user_id=candidate_voted)
				setattr(vote , column, True)
				vote.save()
			return HttpResponseRedirect('/vote/2')
		except:
			pass
