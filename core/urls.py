
from django.urls import path
from .views import home, admin, client, sessinic, adminic, pricng, registro, form_horas

urlpatterns = [

    path('', home, name="home"),
    path('Admin', admin, name="admin"),
    path('Client', client, name="client"),
    path('iniciarSesion', sessinic, name="sessinic"),
    path('inicio_admin', adminic, name="adminic"),
    path('pricing', pricng, name="pricng"),
    path('Registro', registro, name="registro"),
    path('form-horas', form_horas, name="form_horas"),

]