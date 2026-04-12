from django.contrib import admin

from .models import Cliente, Siniestro, Unidad, Marca


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
	list_display = ("nombre",)
	search_fields = ("nombre",)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
	list_display = ("nombre", "direccion", "telefono")
	search_fields = ("nombre", "telefono")


@admin.register(Unidad)
class UnidadAdmin(admin.ModelAdmin):
	list_display = ("modelo", "anio", "numero_poliza", "cliente")
	search_fields = ("modelo", "numero_poliza", "cliente__nombre")
	list_filter = ("anio",)


@admin.register(Siniestro)
class SiniestroAdmin(admin.ModelAdmin):
	list_display = ("numero_siniestro", "fecha_siniestro", "unidad", "monto_estimado", "sospechoso")
	search_fields = ("numero_siniestro", "unidad__numero_poliza", "unidad__cliente__nombre")
	list_filter = ("sospechoso", "fecha_siniestro")
