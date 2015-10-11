from django.shortcuts import render, get_object_or_404
from .models import Candidate
from authentication.models import User
from django.http import HttpResponseRedirect
from .forms import CandidateForm
from django.core.urlresolvers import reverse
from django.contrib import messages

def index(request):
	if request.method=="POST":
		form = CandidateForm(request.POST , request.FILES)
		if form.is_valid():
			try:
				m = Candidate.objects.get(user = request.user)
			print form.cleaned_data["image"]
			print form.cleaned_data["manifesto"]
			try:	
				m = Candidate.objects.create(user = request.user, post = int(form.cleaned_data['post']))
				print "asd"
				m.image = form.cleaned_data["image"]
				m.manifesto = form.cleaned_data["manifesto"]
				m.save()
				messages.success(request , "Your nomination was successful! Best of luck for the upcoming elections!")
				print "yahan bhi!"
				return HttpResponseRedirect('/')
			except:
				print form
				print "Main yahan!"
				return HttpResponseRedirect('.')
	else:
		print request.user.id
		form = CandidateForm()
		return render(request , "candidate/index.html", {'form':form})