## HU-030: Agregar Notas a la Orden desde POS

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario (Owner o Cajero), quiero agregar notas a la orden desde el POS para registrar instrucciones especiales del cliente antes de procesar el pago.

### Criterios de Aceptación

**Campo de Notas en POS:**
- Ubicado en el área del carrito, debajo de la lista de productos
- Antes del resumen de totales
- Label: "Notas" o "Instrucciones especiales"
- Textarea de 2-3 líneas
- Contador de caracteres: "0/500"

**Edición de Notas:**
- El campo es editable en cualquier momento mientras se construye la orden
- Máximo 500 caracteres
- Al alcanzar el límite, no permitir más escritura
- Si se excede en pegado, truncar a 500 caracteres

**Notas en Modal de Pago:**
- Sección "Notas:" con el contenido de las notas

**Notas en Orden Creada:**
- Al completar el pago, las notas se guardan en la orden
- En el detalle de la orden, las notas son visibles
- Las notas se pueden editar después desde el detalle de la orden (solo si no está cerrada)

**Persistencia de Notas:**
- Las notas permanecen en el carrito mientras se agregan/quitan productos
- Las notas NO se limpian automáticamente al completar venta
- Al iniciar nueva venta, limpiar también el campo de notas

**Formato de Notas:**
- Mantener saltos de línea si el usuario los ingresa
- Trimear espacios al inicio y final
- No permitir solo espacios en blanco

**Campo Opcional:**
- Las notas son completamente opcionales
- Se puede procesar pago sin notas

### Escenarios

4. **Contador de caracteres**: Usuario escribe en notas, ve contador actualizar "47/500 caracteres", continúa escribiendo hasta "255/500"
5. **Límite de caracteres**: Usuario escribe 500 caracteres, intenta escribir más, el campo no permite más escritura
6. **Pegar texto largo**: Usuario copia texto de 800 caracteres, lo pega en notas, el sistema trunca automáticamente a 500 caracteres

---
