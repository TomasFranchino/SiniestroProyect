from django import forms

from .models import Cliente, Siniestro, Unidad, Marca


class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = ["nombre", "direccion", "telefono"]


class UnidadForm(forms.ModelForm):
	class Meta:
		model = Unidad
		fields = [
			"cliente",			"marca",			"modelo",
			"anio",
			"valor_auto",
			"numero_poliza",
			"fecha_alta_poliza",
		]
		widgets = {
			"fecha_alta_poliza": forms.DateInput(attrs={"type": "date"}),
		}


class SiniestroForm(forms.ModelForm):
	class Meta:
		model = Siniestro
		fields = [
			"unidad",
			"numero_siniestro",
			"fecha_siniestro",
			"descripcion",
			"monto_estimado",
			"sospechoso",
		]
		widgets = {
			"fecha_siniestro": forms.DateInput(attrs={"type": "date"}),
			"descripcion": forms.Textarea(attrs={"rows": 4}),
		}