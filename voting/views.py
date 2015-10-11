from django.shortcuts import render
from .models import Votes, Positions
from authentication.models import User
from django.http import HttpResponseRedirect
from candidate.models import Candidate

def index(request):
	return render(request, 'voting/index.html')

def details(request , vote_id):
	column = 'vote' + `int(vote_id)`
	if request.method=="GET":
		#application logic to get the standing position and the avaiable candidates
		#default
		if Votes.objects.filter(user_id = request.user.id).exists():
			vote = Votes.objects.get(user_id = request.user.id)
			val = getattr(vote, column)
			if val is True:
				return render(request , 'voting/vote.html', {"cond" : 1})

		position = Positions.objects.get(pk=int(vote_id)).position
		candidates = Candidate.objects.all().filter(post=int(vote_id))
		users = []
		for candidate in candidates:
			users.append(User.objects.get(id = candidate.user_id))
		context = {'position' : position , 'candidates': users}
		return render(request , 'voting/vote.html' , context)
	elif request.method=="POST":
		print column
		candidate_voted = int(request.POST['vote'])
		candidate = Candidate.objects.get(user_id = candidate_voted)
		v = candidate.vote
		v+=1
		candidate.vote = v
		print v
		candidate.save()
		try:
			vote = Votes.objects.get(user_id = request.user.id)
			setattr(vote, column , True)
			vote.save()
		except:
			vote = Votes(user_id=request.user.id)
			setattr(vote , column, True)
			vote.save()
		url = '/vote/' + `int(vote_id)+1`
		return HttpResponseRedirect(url)
