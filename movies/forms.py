from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя пользователя'}))
	email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class SecondCreateUserForm(UserCreationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'}))
	email = forms.CharField(widget=forms.EmailInput())


	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
	username = forms.CharField(widget = forms.TextInput(attrs = {
		'class':'form-control',
		'placeholder': 'Username'
		}))
	password = forms.CharField(widget = forms.PasswordInput(attrs = {
		'class':'form-control',
		'placeholder': 'Password'
		}))