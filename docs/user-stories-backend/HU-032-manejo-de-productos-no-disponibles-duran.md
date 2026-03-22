## HU-032: Manejo de Productos No Disponibles Durante Venta

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario (Owner o Cajero), quiero que el sistema me alerte si un producto se vuelve no disponible mientras estoy construyendo una orden para evitar errores en el proceso de venta.

### Criterios de Aceptación

**Detección de Cambio de Estado:**
- Si un producto en el carrito cambia a "No disponible" (por acción de otro usuario), el sistema debe detectarlo
- La detección ocurre:
  - Durante la validación antes de procesar pago
  - Opcionalmente, en tiempo real con WebSocket/polling

**Alerta de Producto No Disponible:**
- Título: "Producto no disponible"
- Mensaje: "El siguiente producto ya no está disponible: [Nombre del producto]"
- Si son múltiples productos: "Los siguientes productos ya no están disponibles: [Lista]"
- Botones:
  - "Eliminar del carrito" (primario)
  - No permitir continuar con el pago hasta eliminar productos no disponibles

**Botón Procesar Pago Deshabilitado:**

**Eliminación Automática (Opcional):**
- Actualizar totales y permitir continuar con los productos restantes

**Validación al Procesar Pago:**
- Antes de crear la orden, validar en backend que todos los productos están disponibles
- Esta es una validación final de seguridad

**Actualización en Tiempo Real (Ideal):**
- Con WebSocket o polling corto, detectar cambios en disponibilidad de productos
- Actualizar visualmente el carrito si un producto se vuelve no disponible

### Escenarios

---

## Resumen del Flujo del POS

**Flujo Completo de Venta:**
```
```

**Métodos de Pago:**
- **Efectivo**: Requiere monto recibido, calcula cambio automáticamente
- **Tarjeta**: Requiere confirmación de pago autorizado (checkbox)

**Acciones Principales:**
- Agregar producto (click en card)
- Cambiar cantidad (+, -, edición directa)
- Limpiar carrito (con confirmación)
- Nueva venta (limpiar todo)

---

## Navegación en POS

**URLs:**
- `/pos` → Interfaz del punto de venta

**Acceso al POS:**
- Desde menú lateral: "POS"

**Breadcrumb:**
- `/pos`: Dashboard > Punto de Venta

---

## Notas Técnicas

**Persistencia del Carrito:**
- Usar localStorage para persistir entre sesiones
- Estructura de datos: array de productos con { id, nombre, precio, cantidad }
- Incluir notas y timestamp
- Limpiar al completar venta
- Implementar expiración de 24 horas

**Cálculos de Precio:**
- Usar aritmética precisa para dinero (evitar problemas de punto flotante)
- Redondear a 2 decimales
- Validar consistencia entre frontend y backend

**Performance:**
- Lazy loading de imágenes de productos
- Virtualización de lista de productos si hay muchos
- Debounce en búsqueda (300ms)
- Optimizar recálculo de totales

**Validaciones:**
- Backend: Validar disponibilidad de productos antes de crear orden
- Backend: Validar que precios no hayan cambiado
- Backend: Crear orden con estado "Cerrada" directamente

**Estados de Orden desde POS:**
- Las órdenes creadas desde POS se crean con estado "Cerrada" automáticamente
- No pasan por Pendiente/Preparación/Lista (flujo directo de pago)
- Canal: "Mostrador" (fijo)

**Accesibilidad:**
- Controles de cantidad fáciles de tocar
- Alto contraste en elementos importantes
- Atajos de teclado para acciones frecuentes

**Optimización para Tablet:**
- Botones con tamaño mínimo de 44x44px
- Espaciado adecuado entre elementos clickeables
- Scroll suave en lista de productos

**Seguridad:**
- Validar precios en backend (no confiar en frontend)
- Verificar disponibilidad de productos en tiempo real
- Validar que el total calculado coincida con servidor
- Logging de todas las transacciones
