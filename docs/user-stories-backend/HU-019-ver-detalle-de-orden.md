## HU-019: Ver Detalle de Orden

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario (Owner o Cajero), quiero ver el detalle completo de una orden para conocer todos los productos, el estado actual, y poder gestionar la orden.

### Criterios de Aceptación

**Sección: Información de la Orden**
- Card con información general:
  - Número de orden (grande y destacado)
  - Estado actual con badge de color
  - Fecha y hora de creación (formato: "26 de enero, 2026 - 10:30 AM")
  - Canal: "Mostrador" (fijo para MVP)
  - Tiempo transcurrido (ej: "Hace 15 minutos", "Hace 2 horas")

**Sección: Control de Estado**
- Botones de acción según estado actual:
- Los botones son grandes y destacados para fácil acceso

**Sección: Productos de la Orden**
- Lista de productos con:
  - Nombre del producto
  - Cantidad (ej: "x2")
  - Precio unitario
  - Subtotal (cantidad × precio unitario)
  - Subtotal de productos
  - Impuesto (% configurado, ej: "IVA 18%: $5.40")
  - Total final (grande y destacado)

**Formato de Precios:**
- Usar moneda configurada en el sistema
- Formato con separador de miles y 2 decimales (ej: "$45.50")
- Total final en negrita o tamaño mayor

**Sección: Notas de la Orden**
- Las notas aparecen en un área de texto con borde distintivo

**Botón de Impresión:**
- La vista de impresión incluye: número de orden, fecha/hora, productos, total, notas

**Estados de Carga:**
- La carga debe completarse en menos de 2 segundos

**Manejo de Errores:**

**Actualización en Tiempo Real:**
- Si otro usuario cambia el estado de la orden, actualizar automáticamente la vista

**Historial de Estados (Opcional pero Recomendado):**
- Timeline mostrando cambios de estado:
  - "Creada - 10:30 AM"
  - "En preparación - 10:35 AM"
  - "Lista - 10:50 AM"
  - "Cerrada - 11:00 AM"

**Permisos:**
- Tanto Owner como Cajero pueden ver detalle de órdenes
- Ambos pueden cambiar estados de órdenes

### Escenarios

13. **Orden no existe**: Usuario intenta acceder a `/orders/999` (no existe), ve página 404 "Orden no encontrada" con botón "Volver a órdenes"

---
