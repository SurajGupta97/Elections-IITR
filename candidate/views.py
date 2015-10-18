from django.shortcuts import render, get_object_or_404
from .models import Candidate
from authentication.models import User
from django.http import HttpResponseRedirect
from .forms import CandidateForm
from django.core.urlresolvers import reverse
from django.contrib import messages
try:
	from ConfigParser import ConfigParser
except:
	from configparser import ConfigParser
import os

def index(request):
	config = ConfigParser()
	config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)) , '../voting/config.cfg'))
	start = int(config.get("elections" , "start"))

	if start==2:
		return HttpResponseRedirect('/vote/results')
	elif start==1:
		messages.success(request , "Elections have begun!")
		return HttpResponseRedirect('/authentication/profile')
	if request.method=="POST":
		if 'id_image' not in request.POST or 'id_manifesto' not in request.POST or 'id_post' not in request.POST:
			messages.success(request, "*Some fields were left empty.")
			return HttpResponseRedirect('.')
		form = CandidateForm(request.POST , request.FILES)
		if form.is_valid():
			try:	
				m = Candidate.objects.create(user = request.user, post = int(form.cleaned_data['post']))
				m.image = form.cleaned_data["image"]
				m.manifesto = form.cleaned_data["manifesto"]
				m.save()
				messages.success(request , "Your nomination was successful! Best of luck for the upcoming elections!")
				return HttpResponseRedirect('/authentication/profile')
			except:
				#User already has submitted one nomination
				messages.success(request , "You have already submitted one nomination")
				return HttpResponseRedirect('/authentication/profile')
	else:
		if Candidate.objects.filter(user = request.user).exists():
			messages.success(request , "You have already submitted one nomination")
			return HttpResponseRedirect('/authentication/profile')
		form = CandidateForm()
		return render(request , "candidate/index.html", {'form':form})