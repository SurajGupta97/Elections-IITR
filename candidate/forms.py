from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms 
from .models import Candidate

class CandidateForm(ModelForm):
	class Meta:
		model = Candidate
		fields = {"post", "manifesto" , "image"}
