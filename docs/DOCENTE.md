# Guía docente: aprobar y ejecutar localmente

## Propuesta pequeña para nueve grupos
Los temas se acuerdan antes de comenzar; no son encargos oficiales de las fuentes.
Cada grupo hace un formulario, un cálculo, validaciones y pruebas. Una historia basta.

| Grupo | Funcionalidad | Ejemplo de éxito | Validación mínima |
|---|---|---|---|
| 01 | Celsius a Fahrenheit | 0 → 32 | entrada numérica finita |
| 02 | Minutos a horas y minutos | 125 → 2 h 5 min | entero no negativo |
| 03 | Precio con descuento | 100 y 20% → 80 | precio ≥ 0; porcentaje 0–100 |
| 04 | Promedio de tres valores | 4, 5, 6 → 5 | tres números finitos |
| 05 | Área de rectángulo | 3 y 4 → 12 | dimensiones positivas |
| 06 | Contador de palabras | hola mundo → 2 | límite de longitud acordado |
| 07 | Número par o impar | 7 → impar | entero válido |
| 08 | División de un total | 100 entre 4 → 25 | total ≥ 0; personas entero > 0 |
| 09 | Segundos a minutos y segundos | 125 → 2 min 5 s | entero no negativo |

No requieren almacenar datos ni coordinar modelos entre grupos. El ejemplo docente
es otro conversor, separado de las nueve entregas.

## Crear y publicar las once ramas
Desde el ZIP, en esta carpeta:
```bash
git init -b main
git add .
git commit -m "Base local simple"
python scripts/create_branches.py
```
El script crea `integracion` y `grupo_01` ... `grupo_09`, sin cambiar de rama ni
sobrescribir referencias existentes. Requiere un primer commit en `main`.
Configura tu identidad Git si el primer commit la solicita.

Alternativa: el `.bundle` entregado ya contiene el commit y las once ramas:
```bash
git clone ayudantia-flask-simple.bundle ayudantia-flask-simple
cd ayudantia-flask-simple
python scripts/create_branches.py
git remote remove origin
```
En ambas alternativas, crea un repositorio GitHub vacío y reemplaza este URL:
```bash
git remote add origin https://github.com/USUARIO/REPOSITORIO.git
git push -u origin --all
```
No se ha publicado automáticamente. Las ramas de grupo se conservan después del merge.

## Configurar GitHub una vez
Protege `integracion` y `main`: exigir PR, aprobación del ayudante, check `pruebas`,
rama actualizada y conversaciones resueltas; bloquear force push y borrado.
Desactivar eliminación automática de ramas de grupo. Preferir merge commit al squash
para mantener el historial de estas ramas persistentes.
Estas reglas se configuran en GitHub; el YAML por sí solo no impide un merge manual.
Según plan/visibilidad puede variar su disponibilidad. Si no hay protección aplicable,
solo el ayudante mantiene escritura y recibe PR desde forks con rama `grupo_NN`.

## Para cada entrega
1. El grupo abre PR `grupo_NN` → `integracion`.
2. CI ejecuta toda la suite y controla que solo haya cambios en su carpeta, usando
   el script confiable de la rama base. Se rechazan PR de otras ramas hacia integración.
3. Revisas que la función acordada esté implementada, sus pruebas sean reales y
   no guarde datos ni modifique el núcleo. El check no prueba todo esto automáticamente.
4. Con CI verde y revisión aprobada, integras mediante merge commit.
5. En tu equipo pruebas el conjunto en `integracion`:
```bash
git switch integracion
git pull --ff-only origin integracion
python -m pytest
python run.py
```
Usa el Python del entorno virtual si no está activado. Abre el portal, demuestra
la función nueva con datos válidos e inválidos y abre los demás módulos. Detén con
Ctrl+C. Si falla, el grupo corrige en su rama y abre/actualiza PR.
6. Si funciona, abres PR docente `integracion` → `main`, revisas y apruebas.
   Puede hacerse por cada módulo aprobado; las pantallas pendientes permanecen visibles.
7. Ejecutas la versión aprobada localmente:
```bash
git switch main
git pull --ff-only origin main
python run.py
```

No cambies de rama con el servidor ejecutándose: detén, cambia, prueba y arranca.
Mantén árbol limpio antes de cambiar de rama. GitHub no despliega en tu equipo;
el último paso lo realizas tú. No necesitas hosting, Docker, secretos ni base de datos.

## Criterios técnicos de integración (sin nota)
Solo carpeta propia; función pequeña acordada implementada; contrato mínimo respetado;
validación de entradas; pruebas de éxito/límite/error; suite global verde; portal y
otros módulos funcionan; README reproducible y aprobación del ayudante.
Los Blueprints comparten proceso: la revisión debe detectar hooks globales, acceso
a otros módulos y efectos al importar. No son una barrera de seguridad.
No ejecutar código de PR con secretos ni usar `pull_request_target` para ello.
Cambios docentes al núcleo se gestionan aparte; requieren excepción explícita al check
que solo admite ramas de grupo hacia integración. No incluirlos en una entrega grupal.

## Tiempo sugerido
Una sesión para entender el ejemplo y acordar entradas/resultados; otra para construir
formulario y función; otra para pruebas, PR y correcciones. Dejar margen de integración
antes del 26/11/2026, fecha de EVA4 del programa; confirmar fecha docente efectiva.
No se fija un cronograma evaluado ni puntajes sin rúbrica publicada.
