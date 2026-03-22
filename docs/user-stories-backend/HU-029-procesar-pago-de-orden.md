## HU-029: Procesar Pago de Orden

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario (Owner o Cajero), quiero procesar el pago de una orden de forma rápida y sencilla para completar la venta y generar el registro correspondiente.

### Criterios de Aceptación

**Botón Procesar Pago:**
- Ubicado en la parte inferior del carrito
- Texto: "Procesar pago" o "Cobrar"

**Modal de Pago:**
- Título: "Procesar pago"
  - Lista de productos con cantidades y subtotales
  - Subtotal
  - Impuesto
  - Total (destacado, grande)
- Selector de método de pago (tabs o radio buttons):
  - Efectivo
  - Tarjeta
- Campos específicos según método de pago
- Botones:
  - "Cancelar" (secundario)
  - "Completar pago" (primario, grande)

**Pago en Efectivo:**
- Campo: "Monto recibido" (input numérico)
- Permitir monto exacto o mayor

**Cálculo de Cambio:**
- Cambio = Monto recibido - Total

**Pago con Tarjeta:**
- No requiere campos adicionales (el pago se procesa externamente)
- Checkbox: "Confirmo que el pago con tarjeta fue autorizado"
- Mensaje informativo: "Procesa el pago en tu terminal y confirma"

**Validaciones:**
- Efectivo: Validar que el monto recibido sea >= total
- Tarjeta: Validar que el checkbox esté marcado

**Completar Pago:**
- Si es exitoso:
  - Crear orden con estado "Cerrada"
  - Registrar venta con método de pago usado
  - Limpiar carrito

**Modal de Confirmación de Venta:**
- Título: "¡Venta completada!"
- Mensaje: "Orden #XXX registrada exitosamente"
  - Total cobrado
  - Método de pago
  - Cambio (si fue efectivo)
- Botones:
  - "Imprimir ticket" (opcional)
  - "Nueva venta" (primario)

**Manejo de Errores:**
- Los productos permanecen en el carrito

**Cancelar Pago:**
- Los productos permanecen en el carrito
- No se crea orden ni registro de venta

**Atajos de Teclado:**

### Escenarios

---
