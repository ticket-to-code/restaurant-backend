## HU-025: Agregar Productos al Carrito

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario (Owner o Cajero), quiero agregar productos al carrito de forma rápida e intuitiva para construir la orden del cliente eficientemente.

### Criterios de Aceptación

**Agregar Producto desde Catálogo:**
- Cantidad inicial: 1 unidad
- Si el producto ya está en el carrito, incrementar cantidad en 1
- Reproducir sonido de confirmación (opcional, debe poder desactivarse)

**Producto Agregado al Carrito:**
- El producto aparece en la lista de carrito con:
  - Nombre del producto
  - Precio unitario
  - Cantidad inicial: 1
  - Subtotal: precio × cantidad
  - Controles +/- para ajustar cantidad
- Si ya existía, solo incrementar cantidad (no duplicar fila)

**Orden de Productos en Carrito:**
- Los productos aparecen en el orden en que fueron agregados
- Mantener orden consistente mientras se modifican cantidades

**Cálculo Automático de Subtotal:**
- Al agregar producto, el subtotal de ese item se calcula automáticamente (precio × cantidad)
- El subtotal total del carrito se actualiza inmediatamente

**Agregar Múltiples Unidades:**
- Al hacer múltiples clicks en el mismo producto, incrementar cantidad
- Cada click agrega 1 unidad

**Límite de Cantidad (Opcional):**
- Límite máximo de 99 unidades por producto
- Si se alcanza el límite, no permitir agregar más

**Estados de Carga:**
- No hay loading al agregar productos (acción instantánea)
- Solo actualización visual del carrito

**Validaciones:**
- No permitir agregar productos marcados como "No disponible"
- No permitir agregar productos de categorías inactivas

### Escenarios

6. **Agregar hasta límite máximo**: Usuario hace clic 99 veces en "Coca Cola", la cantidad llega a 99, el siguiente click muestra mensaje temporal "Cantidad máxima alcanzada"

---
