## HU-027: Eliminar Productos del Carrito

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario (Owner o Cajero), quiero eliminar productos del carrito para corregir errores o cuando el cliente cambia su orden.

### Criterios de Aceptación

**Botón Eliminar:**
- Posicionado a la derecha de la fila del producto

**Comportamiento al Eliminar:**
- Los totales se recalculan automáticamente

**Actualización de Totales:**
- Al eliminar producto, recalcular:
  - Subtotal general
  - Impuesto
  - Total final
- Si era el único producto, el carrito queda vacío

**Carrito Vacío:**
- Los totales muestran $0.00

**Botón Limpiar Carrito:**

**Modal de Confirmación Limpiar Carrito:**
- Título: "¿Limpiar el carrito?"
- Mensaje: "Se eliminarán todos los productos. Esta acción no se puede deshacer."
- Botones:
  - "Cancelar" (secundario)
  - "Limpiar" (destructivo/rojo)

**Alternativa: Decrementar a 0:**

### Escenarios

---
