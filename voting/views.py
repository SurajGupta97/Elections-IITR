from django.shortcuts import render
from .models import Votes, Positions
from authentication.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages
from candidate.models import Candidate
from django.db.models import Max , F
try:
	from ConfigParser import ConfigParser
except:
	from configparser import ConfigParser
import os

def index(request):
	if request.user.is_authenticated():
		request.session["username"] = request.user.username
		config = ConfigParser()
		config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)) , 'config.cfg'))
		start = int(config.get("elections" , "start"))
		if start==0:
			messages.success(request , "The elections have not yet started.")
			return HttpResponseRedirect('/authentication/profile')
		elif start==2:
			return HttpResponseRedirect('/vote/results')
		return render(request, 'voting/index.html')
	else:
		return HttpResponseRedirect('/authentication/signup')

def details(request , vote_id):
	if request.user.is_authenticated():
		request.session["username"] = request.user.username
		config = ConfigParser()
		config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)) , 'config.cfg'))
		start = int(config.get("elections" , "start"))
		if start==0:
			messages.success(request , "The elections have not yet started.")
			return HttpResponseRedirect('/authentication/profile')
		elif start==2:
			return HttpResponseRedirect('/vote/results')

		if int(vote_id) == 5:
			messages.success(request , "Congrats! You have succesfully completed your voting!")
			return HttpResponseRedirect('/authentication/profile')
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
			if 'vote' not in request.POST:
				messages.success(request , "Please select someone to vote!")
				return HttpResponseRedirect('.')
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
	else:
		return HttpResponseRedirect('/authentication/signup')

def results(request):
	if request.user.is_authenticated():
		request.session["username"] = request.user.username
		config = ConfigParser()
		config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)) , 'config.cfg'))
		start = int(config.get("elections" , "start"))
		if start==2:
			candidates = []
			posts = []
			for p in range(1,5):
				candids = Candidate.objects.filter(post=p)
				post = Positions.objects.get(id = p)
				maxm = 0
				cand = None
				for c in candids:
					if c.votes>=maxm:
						maxm = c.votes
						cand = c
				if cand is not None:	
					user = User.objects.get(id=cand.user_id)
					candidates.append(user)
					posts.append(post)
			return render(request , "voting/results.html" , {"cp" : zip(candidates , posts)})

		else:
			if start==1:
				messages.success(request , "The elections are going on!")
			else:
				messages.success(request , "The elections have not yet started.")
			return HttpResponseRedirect('/authentication/profile')
	else:
		return HttpResponseRedirect('/authentication/signup')