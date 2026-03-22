## HU-020: Cambiar Estado de Orden

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario (Owner o Cajero), quiero cambiar el estado de las órdenes para reflejar el progreso en la preparación y entrega de los pedidos.

### Criterios de Aceptación

**Flujo de Estados:**
- El ciclo de estados es lineal: Pendiente → Preparación → Lista → Cerrada
- No se puede saltar estados (ej: de Pendiente a Lista)
- No se puede retroceder estados (ej: de Preparación a Pendiente)
- Una vez Cerrada, la orden no puede cambiar de estado

**Cambio de Estado desde Lista de Órdenes:**
- En cada fila de la tabla, incluir dropdown o botones rápidos para cambiar estado

**Cambio de Estado desde Detalle:**

**Modal de Confirmación:**
- Título: "¿Cambiar estado de orden?"
- Mensaje según acción:
  - "¿Iniciar preparación de orden #XXX?"
  - "¿Marcar orden #XXX como lista?"
  - "¿Cerrar orden #XXX?"
- Botones:
  - "Cancelar" (secundario)
  - "Confirmar" (primario)

**Comportamiento del Cambio:**
- Si el cambio es exitoso:
  - Actualizar el badge de estado inmediatamente
  - Si está en lista de órdenes, actualizar la fila
  - Si está en detalle, actualizar toda la vista
  - Actualizar contadores en los tabs de filtros

**Manejo de Errores:**
- El estado permanece en el valor anterior

**Validación de Estado Actual:**
- Antes de cambiar, validar en backend que la orden está en el estado esperado
- Esto previene conflictos si múltiples usuarios cambian la misma orden simultáneamente

**Timestamp de Cambios:**
- Registrar fecha y hora de cada cambio de estado
- Registrar usuario que realizó el cambio (Owner o Cajero)
- Esta información se usa para el historial de estados

**Cambios Masivos (en Lista):**
- Permitir seleccionar múltiples órdenes con checkbox
- Aplicar cambio a todas las órdenes seleccionadas simultáneamente

**Atajos de Teclado (Opcional):**
- En detalle de orden, permitir atajos:
  - "P" para Iniciar preparación
  - "L" para Marcar como lista
  - "C" para Cerrar orden

### Escenarios

---
