## HU-034: Ver Detalle de Venta

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario Owner, quiero ver el detalle completo de una venta específica para conocer todos los productos vendidos, el método de pago y otra información relevante de la transacción.

### Criterios de Aceptación

**Sección: Información General**
- Card con información de la venta:
  - Número de orden (grande y destacado)
  - Estado: "Cerrada" (con badge gris)
  - Fecha y hora completa (formato: "26 de enero, 2026 - 10:30 AM")
  - Canal: "Mostrador" (fijo para MVP)
  - Información adicional según método de pago:
    - Efectivo: Monto recibido y cambio entregado
    - Tarjeta: Solo indicador de pago autorizado

**Ejemplo Información Efectivo:**
- "Método de pago: Efectivo"
- "Monto recibido: $50.00"
- "Cambio entregado: $15.78"

**Sección: Productos Vendidos**
- Lista detallada de productos con:
  - Nombre del producto
  - Cantidad (ej: "x2")
  - Precio unitario
  - Subtotal (cantidad × precio unitario)
- Los productos aparecen en el mismo orden que fueron agregados

**Sección: Resumen de Totales**
- Al final de la lista de productos:
  - Subtotal de productos
  - Impuesto (% y monto)
  - Total final (destacado, grande, en negrita)

**Formato de Moneda:**
- Usar moneda configurada en el sistema
- Formato con separador de miles y 2 decimales
- Consistente en toda la página

**Sección: Notas**
- Título: "Notas"
- Contenido de las notas con formato (respetando saltos de línea)

**Botón Imprimir Ticket:**
- La vista incluye:
  - Nombre del restaurante
  - Número de orden
  - Fecha y hora
  - Lista de productos con cantidades y precios
  - Totales
  - Método de pago
  - Notas (si existen)
  - Mensaje de agradecimiento (opcional)

**Vista de Impresión:**
- Formato optimizado para impresora de tickets (58mm o 80mm)
- Texto alineado correctamente
- Sin elementos de navegación
- Sin colores (blanco y negro)

**Estados de Carga:**
- La carga debe completarse en menos de 2 segundos

**Manejo de Errores:**

**Información Inmutable:**
- Toda la información mostrada es de solo lectura
- No hay opciones de edición (la venta está cerrada y completada)
- Los datos son un registro histórico permanente

**Permisos:**
- Solo Owner puede ver detalle de ventas
- Si Cajero intenta acceder, ver página 403

### Escenarios

11. **Venta no encontrada**: Owner intenta acceder a `/sales/999` (no existe), ve página 404 "Venta no encontrada" con botón "Volver al historial"
15. **Cajero intenta acceder**: Usuario Cajero intenta navegar a `/sales/001`, ve página 403 "No tienes permisos para acceder a esta sección"

---
