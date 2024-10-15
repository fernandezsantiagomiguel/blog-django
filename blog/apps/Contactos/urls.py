from django.urls import path
from . import views

app_name = "contactos"

urlpatterns = [
    path("agregar/", views.Cargar_contacto.as_view(), name="agregar_contacto"),
]

