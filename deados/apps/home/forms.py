from django import forms
from django.contrib.auth.models import User
from deados.apps.home.models import Institucion_nombre

class RegisterInstitucionForm(forms.Form): 
	username 		= forms.ModelChoiceField(queryset=Institucion_nombre.objects.all(),label='Nombre de usuario')
	password_one 	= forms.CharField(widget=forms.PasswordInput(render_value=False),label='Contrasena')
	password_two 	= forms.CharField(widget=forms.PasswordInput(render_value=False),label='Confirmar Contrasena')

	def clean_username(self):
		username 	= self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Nombre de usuario ya existe')