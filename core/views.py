from django.shortcuts import render


# Create your views here.

def home(request):
	return render(request, 'core/index.html')

def admin(request):
	return render(request, 'core/Admin.html')

def client(request):
	return render(request, 'core/Client.html')

def sessinic(request):
	return render(request, 'core/iniciarSesion.html')

def adminic(request):
	return render(request, 'core/inicio_admin.html')

def pricng(request):
	return render(request, 'core/pricing.html')

def registro(request):
	return render(request, 'core/Registro.html')


