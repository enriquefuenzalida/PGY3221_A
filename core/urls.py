
from django.urls import path
from .views import home, admin, client, sessinic, adminic, pricng, registro

urlpatterns = [

    path('', home, name="home"),
    path('Admin.html', admin, name="admin"),
    path('Client.html', client, name="client"),
    path('iniciarSesion.html', sessinic, name="sessinic"),
    path('inicio_admin.html', adminic, name="adminic"),
    path('pricing.html', pricng, name="pricng"),
    path('Registro.html', registro, name="registro"),

]
