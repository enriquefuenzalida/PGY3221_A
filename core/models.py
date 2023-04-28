from django.db import models

# Create your models here.

#Modelo para el Hora

class HoraToma(models.Model):
	horaIden = models.CharField(max_length=6,primary_key=True, verbose_name='Identificador')
	horaDate = models.CharField(max_length=20, verbose_name='Fecha')
	horaServ = models.CharField(max_length=20, verbose_name='Servicio')
	
	def __str__(self):
		return self.horaIden
