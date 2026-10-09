# Verificación de la versión simple

08/10/2026 · Windows · Python 3.13.2 · Flask 3.1.2 · pytest 8.3.5.

Comando real: `python -m pytest --basetemp=../../.pruebas-simple -q --tb=short`.
Resultado: **23 pruebas aprobadas**, sin fallos ni pruebas omitidas.

Se comprobó: portal y diez pantallas (nueve grupos más ejemplo), rutas únicas y
delimitadas por módulo, solo métodos de consulta, conversión válida, cero, decimales,
texto inválido, negativos, límites, valores no finitos, resultado/error en HTML y
control de cambios dentro de la carpeta de grupo.

Se ejecutó realmente `python run.py` y se consultó por HTTP local: portal, CSS y
las diez pantallas respondieron 200; 2 km devolvió 2000 metros; texto inválido devolvió
400. El servidor se detuvo al terminar. La aplicación usa únicamente Flask y la
biblioteca estándar; no importa componentes de persistencia ni sesiones.

El entorno de verificación tenía los paquetes de la versión anterior instalados,
pero esta versión no los utiliza ni los declara. No se realizó verificación visual
manual en navegador. GitHub Actions se ejecutará al publicar; todavía no se ha
probado en un remoto ni en Linux. Las pruebas de grupos comprueban pantallas iniciales,
no funcionalidades que aún deben construir los equipos. La aceptación requiere
pruebas propias y demostración del ayudante.

`--basetemp` se usó porque el entorno de ejecución restringe el directorio temporal
predeterminado. No hace falta en un equipo sin esa restricción.
