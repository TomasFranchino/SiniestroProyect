# Proyecto Siniestro - Sistema de Gestión de Siniestros de Autos

Sistema web desarrollado con Django para gestionar datos de clientes, unidades de vehículos y siniestros (accidentes de autos).

## 📋 Descripción del Proyecto

Este proyecto permite:
- Registrar clientes con sus datos (nombre, dirección, teléfono)
- Gestionar unidades (vehículos) asociadas a clientes con marca, modelo, año, valor y póliza
- Registrar siniestros con detalles del accidente, descripción y monto estimado
- Consultar listados de siniestros
- Administrar marcas de vehículos más comunes en Argentina

## 📁 Estructura del Proyecto

```
SiniestroProyect/
├── configuracion/           # Configuraciones de Django
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│   └── __init__.py
├── siniestros/             # Aplicación principal
│   ├── models.py           # Modelos de base de datos
│   ├── views.py            # Vistas de la aplicación
│   ├── forms.py            # Formularios Django
│   ├── urls.py             # URLs de la app
│   ├── admin.py            # Administración Django
│   ├── templates/
│   │   └── siniestros/
│   │       ├── cliente_form.html
│   │       ├── unidad_form.html
│   │       └── siniestro_list.html
│   ├── migrations/         # Migraciones de base de datos
│   │   ├── 0001_initial.py
│   │   ├── 0002_marca_unidad_marca.py
│   │   └── 0003_agregar_marcas_argentina.py
│   ├── tests.py
│   ├── apps.py
│   └── __init__.py
├── manage.py               # Script de gestión de Django
├── db.sqlite3             # Base de datos SQLite
├── .gitignore
├── .venv/                 # Entorno virtual Python
└── README.md              # Este archivo
```

## 🗄️ Modelos de Base de Datos

### Cliente
Información de los clientes propietarios de vehículos.
- `nombre` (CharField): Nombre del cliente (máx. 120 caracteres)
- `direccion` (CharField): Dirección (máx. 255 caracteres)
- `telefono` (CharField): Teléfono de contacto (máx. 30 caracteres)

### Marca
Marcas de vehículos disponibles.
- `nombre` (CharField): Nombre de la marca, único (máx. 100 caracteres)

**Marcas preinstaladas:**
Toyota, Honda, Ford, Chevrolet, Volkswagen, Fiat, Renault, Nissan, Hyundai, Peugeot, Citroën, BMW, Mercedes-Benz, Audi, SEAT, Kia, Suzuki, Mitsubishi, Jeep, Subaru

### Unidad
Vehículos registrados en el sistema.
- `cliente` (ForeignKey): Cliente propietario
- `marca` (ForeignKey): Marca del vehículo
- `modelo` (CharField): Modelo del vehículo (máx. 120 caracteres)
- `anio` (PositiveIntegerField): Año de fabricación
- `valor_auto` (DecimalField): Valor del vehículo (hasta 12 dígitos, 2 decimales)
- `numero_poliza` (CharField): Número de póliza (máx. 50 caracteres)
- `fecha_alta_poliza` (DateField): Fecha de activación de la póliza

### Siniestro
Registro de accidentes y siniestros.
- `unidad` (ForeignKey): Vehículo afectado
- `numero_siniestro` (CharField): Número único del siniestro (máx. 50 caracteres)
- `fecha_siniestro` (DateField): Fecha del accidente
- `descripcion` (TextField): Descripción detallada del siniestro
- `monto_estimado` (DecimalField): Costo estimado (hasta 12 dígitos, 2 decimales)
- `sospechoso` (BooleanField): Indicador de siniestro sospechoso

## 🚀 Instalación y Configuración

### 1. Requisitos Previos
- Python 3.8+
- pip o uv (gestor de paquetes)

### 2. Clonar el Repositorio
```bash
git clone <URL_DEL_REPOSITORIO>
cd SiniestroProyect
```

### 3. Crear Entorno Virtual
```bash
# Con venv
python -m venv .venv

# Activar el entorno virtual
# En Windows (PowerShell):
.venv\Scripts\Activate.ps1

# En macOS/Linux:
source .venv/bin/activate
```

### 4. Instalar Dependencias
```bash
# Opción 1: Con pip
pip install django

# Opción 2: Con uv
uv pip install django
```

### 5. Aplicar Migraciones
```bash
python manage.py migrate
```

Esto creará la base de datos SQLite y todas las tablas necesarias, incluyendo las 20 marcas de Argentina preinstaladas.

## 🎯 Uso

### Ejecutar el Servidor de Desarrollo
```bash
python manage.py runserver
```

El servidor estará disponible en: `http://127.0.0.1:8000/`

### Acceder al Panel de Administración
```
http://127.0.0.1:8000/admin/
```

Usuario y contraseña: Crear mediante:
```bash
python manage.py createsuperuser
```

### URLs Disponibles

| URL | Vista | Descripción |
|-----|-------|-------------|
| `/` | Home | Página principal |
| `/siniestros/cliente/crear/` | ClienteCreateView | Crear nuevo cliente |
| `/siniestros/unidad/crear/` | UnidadCreateView | Crear nueva unidad |
| `/siniestros/siniestro/crear/` | SiniestroCreateView | Registrar nuevo siniestro |
| `/siniestros/` | SiniestroListView | Listar siniestros |
| `/admin/` | Django Admin | Panel de administración |

## 📝 Formularios

### ClienteForm
Campos: nombre, dirección, teléfono

### UnidadForm
Campos: cliente, marca, modelo, año, valor del auto, número de póliza, fecha de alta de póliza
- Campo de marca: Menú desplegable con las marcas disponibles

### SiniestroForm
Campos: unidad, número de siniestro, fecha, descripción, monto estimado, ¿sospechoso?
- Campos de fecha con widget tipo "date"
- Campo descripción con textarea de 4 filas

## 🗂️ Migraciones

El proyecto incluye las siguientes migraciones:

1. **0001_initial.py** - Creación inicial de modelos (Cliente y Unidad iniciales)
2. **0002_marca_unidad_marca.py** - Creación del modelo Marca y relación con Unidad
3. **0003_agregar_marcas_argentina.py** - Inserción de 20 marcas comunes en Argentina

Para crear nuevas migraciones después de cambios en los modelos:
```bash
python manage.py makemigrations
python manage.py migrate
```

## 🔧 Desarrollo

### Shell Interactivo de Django
```bash
python manage.py shell
```

Ejemplos de uso en el shell:
```python
from siniestros.models import Cliente, Marca, Unidad, Siniestro

# Crear cliente
cliente = Cliente.objects.create(nombre="Juan Pérez", direccion="Calle 123", telefono="1234567890")

# Acceder a marcas
marcas = Marca.objects.all()

# Crear unidad
unidad = Unidad.objects.create(
    cliente=cliente,
    marca=Marca.objects.get(nombre="Toyota"),
    modelo="Corolla",
    anio=2020,
    valor_auto=15000.00,
    numero_poliza="POL-001",
    fecha_alta_poliza="2023-01-15"
)

# Registrar siniestro
siniestro = Siniestro.objects.create(
    unidad=unidad,
    numero_siniestro="SIN-001",
    fecha_siniestro="2024-02-20",
    descripcion="Choque frontal en intersección",
    monto_estimado=5000.00,
    sospechoso=False
)
```

## 🌐 Desactivar Entorno Virtual

Para salir del entorno virtual:
```bash
deactivate
```

**Nota:** En PowerShell, si escribes `.\venv\Scripts\deactivate` no funcionará. Simplemente usa `deactivate`.

## 📚 Dependencias

- **Django 6.0.4** - Framework web

Instalar desde `requirements.txt` (si existe):
```bash
pip install -r requirements.txt
```

## 🐛 Solución de Problemas

### Problema: `(venv)` aparece sin color en PowerShell
**Solución:** Es solo un problema visual. Verifica que el entorno esté activo con:
```bash
python --version
where python  # Debe apuntar a .venv\Scripts\python.exe
```

### Problema: Errores al crear migraciones con campos no nulos
**Solución:** Se puede proporcionar un valor por defecto o hacer el campo nullable con `null=True, blank=True`.

### Problema: base de datos vacía después de migraciones
**Solución:** Las migraciones de datos (como la de marcas) se aplican automáticamente. Si no aparecen, ejecuta:
```bash
python manage.py migrate
```

## 📞 Contacto y Soporte

Para reportar issues o sugerencias, contacta al equipo de desarrollo.

---

**Última actualización:** 12 de Abril de 2026
**Versión:** 1.0
