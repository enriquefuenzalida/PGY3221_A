from django import forms
from django.forms import ModelForm
from .models import HoraToma

class HoraTomaForm(ModelForm):
	class Meta:
		model = HoraToma
		fields = ['horaIden','horaDate','horaServ']

		widget = {
			'horaIden': forms.TextInput(attrs={'class':'form-control'}),
			'horaDate': forms.TextInput(attrs={'class':'form-control'}),
			'horaServ': forms.TextInput(attrs={'class':'form-control'}),
		}