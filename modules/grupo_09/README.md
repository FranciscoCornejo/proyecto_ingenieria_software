# Grupo 09 - Módulo de Cotización con Descuento

- **Integrantes:**
  - Matías Cáceres (Matiascaceres7-cpu)
  - Sebastián Galdames (sebastiangaldames-prog)
  - Nicolás Rodríguez (nicolasrodriguez10-design)
- **Representante encargado de publicación:** Sebastián Galdames

---

## 1. Descripción del Módulo
El módulo automatiza el cálculo de cotizaciones comerciales aplicando tramos de descuento escalonados según el volumen de productos solicitados por el cliente.

- **Cómo acceder:** Ingresar localmente en la ruta del servidor Flask: `http://127.0.0.1:5000/modulos/grupo_09/`

## 2. Entradas y Restricciones
- **`cantidad`**: Número entero estrictamente mayor a 0.
- **`precio_unitario`**: Número entero o decimal mayor o igual a 0.

## 3. Ejemplo de Uso (Caso Válido)
- **Entradas:** Cantidad = 20, Precio Unitario = 1000
- **Resultado Esperado:** 
  - Subtotal: $20000.0
  - Descuento aplicado (10%): $2000.0
  - Total a pagar: $18000.0

## 4. Casos Inválidos
Si se ingresa una cantidad menor o igual a 0 (ej. Cantidad = 0), el sistema bloquea el cálculo y despliega una alerta visual con el mensaje: *"Error: La cantidad debe ser un entero mayor a 0."*

## 5. Ejecución de Pruebas Unitarias
Para ejecutar las pruebas unitarias creadas para este módulo, activa tu entorno virtual y corre el siguiente comando en la terminal:
```powershell
pytest modules/grupo_09/tests/test_grupo_09.py