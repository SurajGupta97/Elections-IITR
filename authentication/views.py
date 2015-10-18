from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,Http404
from authentication.forms import UserForm,ProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from authentication.models import UserDetails

def index(request):
	return HttpResponse("Welcome to Elections IITR")

def signup(request):
	if request.user.is_authenticated():
		request.session['username']=request.user.username;
		return HttpResponseRedirect('/authentication/profile')
	elif request.method=="POST":
		signupform=UserForm(request.POST)
		if signupform.is_valid():
			new_user=User.objects.create_user(**signupform.cleaned_data)
			new_user.backend='django.contib.auth.backends.ModelBackend'
			messages.add_message(request,messages.SUCCESS,'Succesfully registered')
			return HttpResponseRedirect('/authentication/signup')
		else:
			return render(request,'authentication/signup.html',{'form':signupform})
	else:
		signupform=UserForm()
		return render(request,'authentication/signup.html',{'form':signupform})

def log_out(request):
	logout(request)
	return HttpResponseRedirect('/authentication/signup/')

def profile(request):
	if request.user.is_authenticated():
		request.session['username']=request.user.username
		try:
			userdetails=get_object_or_404(UserDetails,user=request.user)
		except(Http404):
			return HttpResponseRedirect('/authentication/profile/complete')
		return render(request,'authentication/profile.html',{'profile':userdetails})

	else:
		username=''
		if(request.method=="POST"):
			username=request.POST.get('username')
			password=request.POST.get('password')
			user=authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					request.session['state']="Login Successful"
					request.session['username']=username
					login(request, user)
					try:
						userdetails=get_object_or_404(UserDetails,user=request.user)
					except(Http404):
						return HttpResponseRedirect('/authentication/profile/complete')
					return render(request,'authentication/profile.html',{'profile':userdetails})
				else:
					request.session['state']="Oops! Account not active"
			else:
				messages.add_message(request,messages.ERROR,'Incorrect Login Credentials')
				return HttpResponseRedirect('/authentication/signup/')

		return HttpResponseRedirect('/authentication/signup/')

def profile_complete(request):
	if request.method=="POST":
		form=ProfileForm(request.POST)
		if form.is_valid():
			new_profile=UserDetails.objects.create(user=request.user,branch=request.POST['branch'],en_no=request.POST['en_no'],year=request.POST['year'],gender=request.POST['gender'],dob=request.POST['dob_year']+'-'+request.POST['dob_month']+'-'+request.POST['dob_day'])
			return HttpResponseRedirect('/authentication/signup')	
		else:
			return render(request,'authentication/complete.html',{'form':form})
	else:
		try:
			userdetails=get_object_or_404(UserDetails,user=request.user)
			return HttpResponseRedirect('authentication/signup')
		except(Http404):
			form=ProfileForm()
			return render(request,'authentication/complete.html',{'form':form})

def profile_complete_submit(request):
	if request.method=="POST":
		form=ProfileForm(request.POST)
		if form.is_valid():
			new_profile=UserDetails.objects.create(user=request.user,branch=request.POST['branch'],en_no=request.POST['en_no'],year=request.POST['year'],gender=request.POST['gender'],dob=request.POST['dob_year']+'-'+request.POST['dob_month']+'-'+request.POST['dob_day'])
			return HttpResponseRedirect('/authetication/signup')	
		else:
			return HttpResponseRedirect('/authentication/profile/complete')
	else:
		return HttpResponseRedirect('/authentication/	profile')	

