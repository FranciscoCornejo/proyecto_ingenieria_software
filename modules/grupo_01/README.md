# Grupo 01
Rama: `grupo_01`. Carpeta exclusiva: `modules/grupo_01/`. PR hacia `integracion`.

Completar:
- Funcionalidad acordada y usuario al que ayuda: permite convertir rápidamente un valor numérico entre distintas unidades utilizando una lista predefinida (por ejemplo, Kilogramos a Gramos o Kilómetros a Metros). Ayuda a los usuarios operativos del sistema a realizar cálculos de equivalencia de manera inmediata, evitando los errores que ocurren al calcular factores de conversión manualmente en calculadoras externas.

- Entradas y límites permitidos: Recibe dos entradas: un campo numérico decimal/float llamado "valor" y una opción de texto llamada "tipo_conversion" obtenida de una lista desplegable fija. El límite permitido para el "valor" es que debe ser estrictamente mayor a 0 y tener un tope máximo de 1.000.000

- Resultado esperado (un ejemplo concreto): Si el usuario ingresa el valor 2.5 y selecciona la opción "Kilogramos a Gramos", el sistema calcula el factor internamente y devuelve en pantalla el mensaje: "2.5 Kilogramos equivalen a 2500.0 Gramos", redondeando el resultado a un máximo de dos decimales.

- Casos inválidos y mensaje esperado: Se considera un caso inválido si el usuario ingresa un número negativo (como -15), el valor 0 o deja el campo vacío. El sistema rechazará el cálculo y mostrará el mensaje esperado en pantalla: "El valor debe ser un número mayor a cero."

- Pruebas agregadas y cómo demostrar la función: Se agregaron casos de prueba mediante Pytest para validar el comportamiento correcto frente a entradas válidas, límites (1.000.000) e inválidas (-15). La función se demostrará de dos formas: primero, ejecutando python -m pytest en la terminal local para comprobar que los tests pasan; y segundo, levantando el entorno de Flask en http://127.0.0.1:5000/modulos/grupo_01

- Responsabilidades y cambios de los integrantes: Se mantienen los roles definidos durante el Hito 1 y 2 sin modificaciones.

La pantalla inicial no es la entrega terminada. Implementar una función pequeña
que reciba datos del formulario y muestre un resultado, sin guardar información.
