## HU-026: Modificar Cantidad de Productos en Carrito

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario (Owner o Cajero), quiero ajustar las cantidades de productos en el carrito para corregir la orden según lo que el cliente solicite.

### Criterios de Aceptación

**Controles de Cantidad:**
- Cada producto en el carrito tiene 3 controles:
  - Campo de cantidad (editable, numérico)

**Incrementar Cantidad (+):**
- El subtotal del producto se actualiza automáticamente
- El total general se recalcula inmediatamente
- Límite máximo: 99 unidades

**Decrementar Cantidad (-):**
- Si la cantidad llega a 0, eliminar el producto del carrito automáticamente
- El subtotal y total se actualizan automáticamente

**Edición Directa de Cantidad:**
- El campo de cantidad es editable (input numérico)
- Al escribir, validar que solo sean números
- Al perder focus (blur), validar y aplicar la cantidad

**Validaciones en Edición Directa:**
- Solo permitir números enteros positivos
- Si se ingresa 0 o se deja vacío, eliminar el producto del carrito
- Si se excede 99, ajustar automáticamente a 99
- Si se ingresa texto no numérico, mantener cantidad anterior

**Actualización de Totales:**
- Al cambiar cantidad, recalcular:
  - Subtotal del producto (precio × cantidad)
  - Subtotal general (suma de todos los subtotales)
  - Impuesto (subtotal × %)
  - Total final (subtotal + impuesto)
- La actualización debe ser instantánea (sin delay)

**Atajos de Teclado (Opcional):**
- Al editar cantidad, permitir:
  - Enter: Aplicar cantidad y mover a siguiente campo
  - Escape: Cancelar edición y mantener cantidad anterior
  - Flechas arriba/abajo: Incrementar/decrementar

### Escenarios

5. **Edición con texto inválido**: Usuario intenta escribir "abc" en cantidad, el campo no acepta letras, mantiene el valor anterior
8. **Exceder límite máximo**: Usuario escribe "150" en cantidad, al hacer blur el sistema ajusta automáticamente a 99
9. **Incrementar hasta límite**: Usuario hace clic 98 veces en "+" de producto con cantidad 1, llega a 99, el siguiente click no hace nada o muestra mensaje

---
