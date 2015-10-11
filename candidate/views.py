from django.shortcuts import render, get_object_or_404
from .models import Candidate
from authentication.models import User
from django.http import HttpResponseRedirect
from .forms import CandidateForm
from django.core.urlresolvers import reverse

def index(request):
	# try:
	# 	candidate = get_object_or_404(Candidate , user_id= 1)
	# except:
	# 	# candidate = Candidate.objects.create(user_id=1)
	if request.method=="POST":
		form = CandidateForm(request.POST , request.FILES)
		if form.is_valid():
			print(form.cleaned_data["image"])
			print(form.cleaned_data["manifesto"])
			try:
				m = Candidate.objects.get(user = request.user)
				m.image = form.cleaned_data["image"]
				m.manifesto = form.cleaned_data["manifesto"]
				m.save()
			except:
				#User already has submitted one nomination
				return HttpResponseRedirect('/')
	else:
		form = CandidateForm()
		return render(request , "candidate/index.html", {'form':form})