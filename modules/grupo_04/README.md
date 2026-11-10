# Grupo 04 · Disponibilidad de cupos

Módulo del proyecto integrador **Study** (Ingeniería de Software). Calcula cuántos cupos quedan disponibles para una actividad o servicio a partir de la capacidad total y los cupos ocupados.

| | |
|---|---|
| **Repositorio** | https://github.com/FranciscoCornejo/proyecto_ingenieria_software.git |
| **Rama** | `grupo_04` |
| **Carpeta** | `modules/grupo_04` |
| **Ruta local** | `http://127.0.0.1:5000/modulos/grupo_04/` |

## Integrantes y roles

| Integrante | Usuario de GitHub | Rol |
|---|---|---|
| Ricardo Chirinos | [RicardoACB](https://github.com/RicardoACB) | Responsabilidad técnica |
| José Reyes | [YOSEPRK](https://github.com/YOSEPRK) | Coordinación |
| Jhan Cabrera | [jhancabrera-lgtm](https://github.com/jhancabrera-lgtm) | Pruebas |
| Juan Montoya | [juanmontoya-beep](https://github.com/juanmontoya-beep) | Desarrollo |

Los roles se mantienen respecto del Hito 1.

## Problema y usuario

Permite saber en todo momento cuál es el máximo de cupos que se pueden vender, evitando la venta de cupos inexistentes. El software lo usa para decidir cuándo cerrar la venta.

La lógica central es una resta, no requiere base de datos ni servicios externos, por lo que el alcance es realizable.

## Funcionalidad

1. El usuario ingresa en un formulario la **capacidad total** y los **cupos ocupados**.
2. El sistema valida que ambos sean enteros no negativos y que los cupos ocupados no superen la capacidad total.
3. Calcula `capacidad_total - cupos_ocupados` y muestra el resultado en pantalla.
4. Si el resultado es `0`, indica que **no quedan cupos disponibles**.

## Entradas y salidas

### Entradas

| Campo | Tipo | Unidad | Valores permitidos |
|---|---|---|---|
| `capacidad_total` | Entero sin signo | Cupos | 0 a 100 (ajustable según el contexto) |
| `cupos_ocupados` | Entero sin signo | Cupos | 0 hasta `capacidad_total` |

**Validaciones (ambos campos):**

- **Obligatoriedad:** no puede ser nulo ni vacío.
- **Formato:** solo caracteres numéricos (se rechazan letras, símbolos y espacios).
- **Tipo:** debe ser un entero exacto.
- **Regla de negocio:** no puede ser menor que 0.
- **Límite:** `cupos_ocupados` no puede ser mayor que `capacidad_total`.

No se aplica redondeo.

### Salida

| Campo | Tipo | Unidad | Valores | Cálculo |
|---|---|---|---|---|
| `cupos_disponibles` | Entero sin signo | Cupos | 0 hasta `capacidad_total` | `capacidad_total - cupos_ocupados` |

## Qué muestra la pantalla

- **Resultado:** la cantidad de cupos disponibles.
- **Estado especial:** mensaje de "no hay cupos" cuando el resultado es 0.
- **Errores:** mensaje de error ante datos inválidos.

## Fuera de alcance

- **Base de datos:** no se guardan consultas ni cálculos.
- **Pagos:** no hay cobros ni transacciones.
- **Reservas:** no se reservan ni apartan cupos en tiempo real.

## Organización del módulo

```
modules/grupo_04/
├── logic.py              # calcular_cupos_disponibles(capacidad_total, cupos_ocupados)
├── routes.py             # Blueprint del grupo y función index (/modulos/grupo_04/)
├── templates/grupo_04/   # Plantilla con formulario, resultado o mensaje de error
└── tests/
    └── test_grupo_04.py  # Pruebas con pytest
```

- `logic.py` valida los valores y calcula los cupos restantes.
- `index` recibe los datos del formulario y llama a la función mediante importación local (`from .logic import calcular_cupos_disponibles`).
- La plantilla propia muestra el formulario, el resultado o el error.

## Casos de prueba

| Caso | Entrada | Resultado esperado |
|---|---|---|
| Válido | `capacidad_total = 100`, `cupos_ocupados = 30` | `cupos_disponibles = 70` |
| Límite | `capacidad_total = 50`, `cupos_ocupados = 50` | `cupos_disponibles = 0` |
| Inválido | `capacidad_total = 20`, `cupos_ocupados = 40` | Error: "los cupos ocupados sobrepasan la capacidad de cupos disponibles" |

Las pruebas también cubren valores negativos y tipos inválidos (texto, decimales).

## Cómo ejecutar

```bash
# Ejecutar el proyecto
flask run          # o el comando indicado en el README del proyecto base
# Abrir http://127.0.0.1:5000/modulos/grupo_04/

# Ejecutar las pruebas
.\.venv\Scripts\python.exe -m pytest
```

## Estado del avance (Hito 2)

- Proyecto clonado, rama `grupo_04` activa y sincronizada con `origin/grupo_04`.
- Portal y pantalla inicial del módulo funcionando en local.
- Pruebas de la base: 23 pruebas pasadas, sin fallas.
- Commit de prueba en `logic.py` (`docs: Confirmacion de commit`).

## Próximas tareas

| Tarea | Responsable / respaldo | Resultado verificable |
|---|---|---|
| Desarrollar la lógica para obtener los cupos disponibles | Juan / José | Commits remotos en `grupo_04` |
| Probar con pytest que la lógica funcione correctamente | Ricardo / Juan | Capturas del estado de las pruebas e informe de fallas o mejoras |
| Crear Excel de horarios de trabajo y revisar el trabajo de los demás | José / Ricardo | Excel de horarios e informes de avance |

## Condiciones de integración

- Solo se modifica `modules/grupo_04/`.
- Se conservan el Blueprint del grupo, la función `index` y las plantillas bajo `templates/grupo_04/`.
- Se usan importaciones locales y variables locales por petición.
- No se cambia el núcleo, las dependencias ni archivos de otros grupos.