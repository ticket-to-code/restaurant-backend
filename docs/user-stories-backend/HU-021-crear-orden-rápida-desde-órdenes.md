## HU-021: Crear Orden Rápida desde Órdenes

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario (Owner o Cajero), quiero poder crear una nueva orden rápidamente desde la página de órdenes para agilizar el flujo de trabajo sin necesariamente ir al POS completo.

### Criterios de Aceptación

**Trigger de Creación:**

**Redirección al POS:**
- El POS está vacío y listo para agregar productos
- Después de crear y cerrar la orden en el POS, volver automáticamente a `/orders`

**Mini-POS Modal (Alternativa):**
  - Título: "Nueva orden"
  - Selector de productos con búsqueda rápida
  - Lista de productos agregados con cantidad y subtotal
  - Campo opcional para notas
  - Total calculado en tiempo real
  - Botones: "Cancelar" y "Crear orden"

**Funcionalidad del Mini-POS:**
- Búsqueda de productos por nombre
- Click en producto lo agrega a la orden
- Botones +/- para ajustar cantidad
- Campo de notas opcional
- Cálculo automático de subtotal, impuesto y total

**Creación de Orden:**
- La orden se crea con estado "Pendiente"
- Canal: "Mostrador" (fijo)
- Actualizar la lista de órdenes mostrando la nueva orden

**Validaciones:**

**Manejo de Errores:**

**Número de Orden Automático:**
- Generar número de orden automáticamente de forma secuencial
- Formato: #001, #002, #003, etc.
- Reiniciar numeración cada día (opcional) o mantener secuencia continua

### Escenarios

---
