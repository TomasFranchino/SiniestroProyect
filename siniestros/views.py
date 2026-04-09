from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from .forms import ClienteForm, SiniestroForm, UnidadForm
from .models import Cliente, Siniestro, Unidad


class ClienteCreateView(CreateView):
	model = Cliente
	form_class = ClienteForm
	template_name = "siniestros/cliente_form.html"
	success_url = reverse_lazy("siniestros:unidad_create")


class UnidadCreateView(CreateView):
	model = Unidad
	form_class = UnidadForm
	template_name = "siniestros/unidad_form.html"
	success_url = reverse_lazy("siniestros:siniestro_create")


class SiniestroListView(ListView):
	model = Siniestro
	template_name = "siniestros/siniestro_list.html"
	context_object_name = "siniestros"

	def get_queryset(self):
		queryset = (
			Siniestro.objects.select_related("unidad", "unidad__cliente")
			.all()
			.order_by("-fecha_siniestro")
		)

		solo_sospechosos = self.request.GET.get("sospechoso")
		cliente = self.request.GET.get("cliente", "").strip()
		poliza = self.request.GET.get("poliza", "").strip()

		if solo_sospechosos:
			queryset = queryset.filter(sospechoso=True)
		if cliente:
			queryset = queryset.filter(unidad__cliente__nombre__icontains=cliente)
		if poliza:
			queryset = queryset.filter(unidad__numero_poliza__icontains=poliza)

		return queryset

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["filtro_sospechoso"] = bool(self.request.GET.get("sospechoso"))
		context["filtro_cliente"] = self.request.GET.get("cliente", "")
		context["filtro_poliza"] = self.request.GET.get("poliza", "")
		return context


class SiniestroCreateView(CreateView):
	model = Siniestro
	form_class = SiniestroForm
	template_name = "siniestros/siniestro_form.html"
	success_url = reverse_lazy("siniestros:siniestro_list")

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["has_unidades"] = Unidad.objects.exists()
		return context

	def form_valid(self, form):
		if not Unidad.objects.exists():
			messages.error(
				self.request,
				"Debes crear al menos una unidad antes de registrar un siniestro.",
			)
			return redirect("siniestros:siniestro_create")
		return super().form_valid(form)


class SiniestroUpdateView(UpdateView):
	model = Siniestro
	form_class = SiniestroForm
	template_name = "siniestros/siniestro_form.html"
	success_url = reverse_lazy("siniestros:siniestro_list")

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["has_unidades"] = Unidad.objects.exists()
		return context
