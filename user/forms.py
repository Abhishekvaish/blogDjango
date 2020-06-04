from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import	 Profile


class UserRegisterationForm(UserCreationForm):
	email = forms.EmailField()
	first_name = forms.CharField(max_length=50)
	last_name = forms.CharField(max_length=50)

	class Meta:
		model = get_user_model()
		fields = ['first_name','last_name','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = get_user_model()
		fields = ['email','first_name','last_name']

class ProfileUpdateForm(forms.ModelForm	):
	class Meta:
		model = Profile	
		fields	= ['img']
