# Ayudantía Flask — versión simple y local

Un portal, nueve funcionalidades pequeñas y un ejemplo docente. Cada grupo
recibe entradas en un formulario y muestra un resultado calculado con Python.
**Sin base de datos, sin guardar archivos de datos, sin cuentas y sin servicios externos.**
No hay instalación de frontend ni Node. El HTML se genera en el servidor con Jinja.

## Levantar en Windows (PowerShell)
Entrar a esta carpeta, donde están `run.py` y este README. Python 3.13 propuesto
para la base y validado con 3.13.2; no es una exigencia atribuida al programa.

Primera vez:
```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
```
Cada vez que quieras abrir el proyecto:
```powershell
.\.venv\Scripts\python.exe run.py
```
Abrir http://127.0.0.1:5000 y detener con Ctrl+C. Solo accesible desde este equipo.
En macOS/Linux usar `.venv/bin/python` en lugar de `.\.venv\Scripts\python.exe`.
No necesitas activar el entorno con estos comandos: se invoca su Python directamente.

Pruebas:
```powershell
.\.venv\Scripts\python.exe -m pytest
```

## Archivos importantes
```text
app.py                 núcleo docente: descubre módulos y genera el menú
run.py                 arranque local
templates/             portal y diseño común
static/                estilos comunes
modules/ejemplo/       conversor funcional de kilómetros a metros
modules/grupo_01/      espacio exclusivo del grupo 1
... grupo_02 a grupo_09/
tests/                 pruebas compartidas
scripts/               ramas y control de carpeta
.github/               pruebas automáticas en GitHub
docs/                  guías cortas
```

El estudiante solo edita su carpeta `modules/grupo_NN/`. Se incorpora automáticamente
al arrancar el proyecto: no edita rutas, menú ni configuración del núcleo.
Las nueve carpetas son pantallas iniciales; cada equipo debe implementar su función.

## Flujo
`grupo_NN` → PR a `integracion` → revisión/pruebas locales → PR docente a `main`
→ ejecutar `main` localmente con `python run.py`.
Se puede promover cada módulo aprobado; no hay que esperar a los nueve grupos.
GitHub conserva código y ejecuta pruebas. La aplicación corre en el equipo local.

- [Cómo funciona y qué editar](docs/ESTUDIANTES.md)
- [Ramas, integración y ejecución local](docs/DOCENTE.md)
- [Fuentes y alcance](docs/FUENTES.md)
- [Verificación realizada](docs/VERIFICACION.md)

La ejecución local es para clase y demostración. El servidor incluido de Flask no
es una configuración para publicar el sitio en internet.
