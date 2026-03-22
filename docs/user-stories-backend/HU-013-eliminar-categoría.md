## HU-013: Eliminar Categoría

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario Owner, quiero eliminar categorías que ya no necesito para mantener el menú organizado y limpio, con la seguridad de que no puedo eliminar categorías que tienen productos asociados.

### Criterios de Aceptación

**Trigger de Eliminación:**

**Tooltip para Botón Deshabilitado:**

**Modal de Confirmación:**
- Mensaje: "¿Estás seguro de que deseas eliminar la categoría '[Nombre]'? Esta acción no se puede deshacer."
- Botones:
  - "Cancelar" (secundario, izquierda)
  - "Eliminar" (destructivo/rojo, derecha)

**Comportamiento de Eliminación:**
- Si la eliminación es exitosa:

**Manejo de Errores:**

**Validación de Backend:**
- Esto previene condiciones de carrera (ej: se agrega producto mientras se intenta eliminar)

**Estado Vacío Después de Eliminar:**

**Cierre del Modal de Confirmación:**
- Al presionar ESC, cerrar sin eliminar

### Escenarios

---
