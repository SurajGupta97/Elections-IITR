from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from authentication.models import UserDetails

class UserForm(ModelForm):
	class Meta:
		model= User
		fields=('username','first_name','last_name','password','email')
		widgets={'password':forms.PasswordInput()}

class ProfileForm(ModelForm):
	class Meta:
		model=UserDetails
		fields=('branch','en_no','gender','dob','year')
		widgets={'gender':forms.RadioSelect(),'dob':SelectDateWidget(years=range(1980,2000)),'branch':forms.RadioSelect(),'year':forms.RadioSelect()}

