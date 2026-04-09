from django.urls import path

from .views import (
	ClienteCreateView,
	SiniestroCreateView,
	SiniestroListView,
	SiniestroUpdateView,
	UnidadCreateView,
)

app_name = "siniestros"

urlpatterns = [
	path("", SiniestroListView.as_view(), name="siniestro_list"),
	path("clientes/nuevo/", ClienteCreateView.as_view(), name="cliente_create"),
	path("unidades/nuevo/", UnidadCreateView.as_view(), name="unidad_create"),
	path("nuevo/", SiniestroCreateView.as_view(), name="siniestro_create"),
	path("<int:pk>/editar/", SiniestroUpdateView.as_view(), name="siniestro_update"),
]