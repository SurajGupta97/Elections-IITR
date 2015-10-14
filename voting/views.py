from django.shortcuts import render
from .models import Votes, Positions
from authentication.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages
from candidate.models import Candidate
try:
	from ConfigParser import ConfigParser
except:
	from configparser import ConfigParser
import os

def index(request):
	config = ConfigParser()
	config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)) , 'config.cfg'))
	start = int(config.get("elections" , "start"))
	if start==0:
		messages.success(request , "The elections have not yet started! :p")
		return HttpResponseRedirect('/')
	return render(request, 'voting/index.html')

def details(request , vote_id):
	config = ConfigParser()
	config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)) , 'config.cfg'))
	start = int(config.get("elections" , "start"))
	if start==0:
		messages.success(request , "The elections have not yet started! :p")
		return HttpResponseRedirect('/')

	column = 'vote' + str(vote_id)
	url = '/vote/' + str(int(vote_id)+1)
	if request.method=="GET":
		#application logic to get the standing position and the avaiable candidates
		#default
		if Votes.objects.filter(user_id = request.user.id).exists():
			vote = Votes.objects.get(user_id = request.user.id)
			val = getattr(vote, column)
			if val is True:
				return HttpResponseRedirect(url)

		position = Positions.objects.get(pk=int(vote_id)).position
		candidates = Candidate.objects.all().filter(post=int(vote_id))
		users = []
		for candidate in candidates:
			users.append(User.objects.get(id = candidate.user_id))
		context = {'position' : position , 'candidates': users}
		return render(request , 'voting/vote.html' , context)
	elif request.method=="POST":
		candidate_voted = int(request.POST['vote'])
		candidate = Candidate.objects.get(user_id = candidate_voted)
		v = candidate.votes
		v+=1
		candidate.votes = v
		candidate.save()
		try:
			vote = Votes.objects.get(user_id = request.user.id)
			setattr(vote, column , True)
			vote.save()
		except:
			vote = Votes(user_id=request.user.id)
			setattr(vote , column, True)
			vote.save()
		return HttpResponseRedirect(url)
