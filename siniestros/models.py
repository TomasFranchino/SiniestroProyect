from django.db import models


class Cliente(models.Model):
	nombre = models.CharField(max_length=120)
	direccion = models.CharField(max_length=255)
	telefono = models.CharField(max_length=30)

	def __str__(self):
		return self.nombre


class Unidad(models.Model):
	cliente = models.ForeignKey(
		Cliente,
		on_delete=models.CASCADE,
		related_name="unidades",
	)
	modelo = models.CharField(max_length=120)
	anio = models.PositiveIntegerField()
	valor_auto = models.DecimalField(max_digits=12, decimal_places=2)
	numero_poliza = models.CharField(max_length=50)
	fecha_alta_poliza = models.DateField()

	def __str__(self):
		return f"{self.modelo} - Poliza {self.numero_poliza}"


class Siniestro(models.Model):
	unidad = models.ForeignKey(
		Unidad,
		on_delete=models.CASCADE,
		related_name="siniestros",
	)
	numero_siniestro = models.CharField(max_length=50, unique=True)
	fecha_siniestro = models.DateField()
	descripcion = models.TextField()
	monto_estimado = models.DecimalField(max_digits=12, decimal_places=2)
	sospechoso = models.BooleanField(default=False)

	def __str__(self):
		return f"Siniestro {self.numero_siniestro}"
