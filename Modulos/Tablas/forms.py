from django import forms
from .models import Empleado, Instalacion, Bitacora, Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class EmpleadoForm(forms.ModelForm):

	class Meta:
		model = Empleado
		fields = "__all__"
		widgets = {
    	'fecha_registro': forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),}		

class InstalacionForm(forms.ModelForm):

	class Meta:
		model = Instalacion
		fields = "__all__"
		widgets = {
    	'fecha_instalacion': forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),}		

class UsuarioForm(UserCreationForm):
	class Meta:
		model = User #this is the "YourCustomUser" that you imported at the top of the file  
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'archivo', 'telefono', 'bio') #etc etc, other fields you want displayed on the form)

class UsuarioFormEdit(forms.ModelForm):
	class Meta:
		model = User #this is the "YourCustomUser" that you imported at the top of the file  
		fields = ('username', 'first_name', 'last_name', 'email', 'archivo', 'telefono', 'bio') #

class BitacoraForm(forms.ModelForm):

	class Meta:
		model = Bitacora
		fields = "__all__"
		widgets = {
    	'fecha_cambio': forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),}		