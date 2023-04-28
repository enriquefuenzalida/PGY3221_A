from django.shortcuts import render, redirect
from .models import HoraToma
from .forms import HoraTomaForm

# Create your views here.

def home(request):
	return render(request, 'core/index.html')

def nav(request):
	return render(request, 'core/nav.html')

def admin(request):
	return render(request, 'core/Admin.html')

def client(request):
	return render(request, 'core/Client.html')

def sessinic(request):
	return render(request, 'core/iniciarSesion.html')

def adminic(request):
	return render(request, 'core/inicio_admin.html')

def pricng(request):
	horaslista = HoraToma.objects.all()
	datos = {
		'lashoras' : horaslista
	}
	return render(request, 'core/pricing.html', datos)

def registro(request):
	return render(request, 'core/Registro.html')

def form_horas(request):
	datos = {
		'form': HoraTomaForm()
	}
	if request.method == 'POST':
		formulario = HoraTomaForm(request.POST)
		if formulario.is_valid:
			formulario.save()
			datos['mensaje'] = "Guardados correctamente"
	return render(request, 'core/form_horas.html', datos)
