# Tu módulo en tres archivos

## 1. Trabajar en tu rama
Clona el repositorio y prepara el entorno siguiendo el README. Para grupo 1:
```bash
git fetch origin
git switch --track origin/grupo_01
```
Si ya existe localmente, usa `git switch grupo_01`. Con cambios guardados en commits
y árbol limpio, antes de cada sesión:
```bash
git fetch origin
git merge origin/grupo_01
git merge origin/integracion
```

## 2. Implementar dentro de tu carpeta
```text
modules/grupo_01/
├── __init__.py                  recibe el formulario y devuelve HTML
├── logic.py                     función Python que calcula el resultado
├── templates/grupo_01/index.html formulario y resultado
├── tests/test_grupo_01.py        pruebas de la función
└── README.md                    explicación breve y casos de ejemplo
```

Mira `modules/ejemplo/`: convierte kilómetros a metros y muestra el patrón completo.
En `logic.py`, una función recibe valores, valida y retorna un resultado. Si los
datos son inválidos, lanza `ValueError` con un mensaje claro.
En `__init__.py`, `request.args.get('campo', '')` lee un valor del formulario GET;
se llama a la función y `render_template(...)` entrega sus datos al HTML.
En la plantilla, `{{ result }}` muestra el resultado y `{% if error %}` el mensaje.

## Reglas mínimas
- Solo modifica `modules/grupo_NN/` de tu grupo. No cambies núcleo, CI o dependencias.
- Conserva `bp` y su nombre `grupo_NN`; conserva la función `index` en la ruta `/`.
- Cambia `TITLE` por el nombre de tu funcionalidad. El portal lo muestra solo.
- Guarda plantillas en `templates/grupo_NN/` y extiende `base.html`.
- Formularios con `method="get"`; el módulo calcula sin modificar datos del servidor.
- No uses SQLite, listas globales para guardar resultados, archivos de datos,
  sesiones, login, APIs externas o paquetes adicionales.
- Valida los datos también en Python, aunque el formulario tenga `required`.
- Prueba una entrada válida, un caso límite y una inválida.

El núcleo define `/modulos/grupo_NN/` automáticamente. No declares `url_prefix`.
Las entradas GET aparecen en la dirección del navegador; usa solamente valores
de práctica, nunca información personal o sensible. El proyecto no las almacena,
pero el navegador puede conservarlas en el historial y el servidor mostrarlas en logs.

## 3. Probar y enviar
Ejecuta toda la suite con el Python del entorno:
```bash
python -m pytest
git add modules/grupo_01
git commit -m "Agrega conversión y pruebas del módulo"
git push origin grupo_01
```
Si no activaste el entorno, sustituye `python` por el comando del README.
En GitHub abre PR de `grupo_01` hacia `integracion`, completa la plantilla y pide
revisión al ayudante. Corrige observaciones en la misma rama. No hagas force push.
No basta que pase la prueba inicial: esa prueba solo abre la pantalla vacía.
Cada vez que cambies código, detén y vuelve a ejecutar `run.py`, luego recarga el
navegador: el arranque simple no reinicia automáticamente.

## Qué ocurre con el resultado
El formulario pide un cálculo → Python calcula → devuelve una página con el resultado.
No hay almacenamiento de resultados. Si vuelves al portal y abres el módulo sin
parámetros, aparece vacío. Si recargas una URL que ya contiene entradas, se calcula
de nuevo; eso no significa que exista una base de datos.
