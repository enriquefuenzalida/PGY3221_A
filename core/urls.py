
from django.urls import path
from .views import home, admin, client, sessinic, adminic, pricng, registro, estilo2css, maincss, registroHoracss, stylescss

urlpatterns = [
    path('', home, name="home"),
    path('Admin.html', admin, name="admin"),
    path('Client.html', client, name="client"),
    path('iniciarSesion.html', sessinic, name="sessinic"),
    path('inicio_admin.html', adminic, name="adminic"),
    path('pricing.html', pricng, name="pricng"),
    path('Registro.html', registro, name="registro"),

    path('estilo2.css', estilo2css, name="estilo2css"),
    path('main.css', maincss, name="maincss"),
    path('registroHora.css', registroHoracss, name="registroHoracss"),
    path('styles.css', stylescss, name="stylescss"),
]
