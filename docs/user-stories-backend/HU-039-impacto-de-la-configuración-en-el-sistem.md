## HU-039: Impacto de la Configuración en el Sistema

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario Owner, necesito que los cambios en la configuración se apliquen correctamente en todas las partes del sistema donde se utilizan estos valores.

### Criterios de Aceptación

**Uso del Nombre del Restaurante:**
- Se muestra en:
  - Header/navbar de la aplicación (opcional)
  - Tickets de venta impresos
  - Facturas (si aplica)
  - Emails automáticos (si aplica)
  - Footer de exportaciones (opcional)
- Actualización: Inmediata al guardar

**Uso de la Dirección:**
- Se muestra en:
  - Tickets de venta impresos (si está configurada)
  - Facturas (si aplica)
  - Información de contacto (si aplica)
- Actualización: Inmediata al guardar

**Uso de la Moneda:**
- Se aplica en:
  - Todos los precios de productos (menú)
  - Totales en POS
  - Totales en órdenes
  - Totales en historial de ventas
  - Reportes y exportaciones
  - Dashboard (KPIs)
- El símbolo de moneda ($, €, S/) se muestra antes o después del número según convención
- Actualización: Inmediata al guardar (refrescar vistas abiertas)

**Uso del Impuesto:**
- Se aplica en:
  - Cálculo de totales en POS (nuevas ventas)
  - Cálculo de totales en órdenes nuevas
  - Resumen de ventas (nuevas)
- NO se aplica retroactivamente a:
  - Ventas anteriores (mantienen su impuesto original)
  - Órdenes cerradas (mantienen su impuesto original)
- Actualización: Inmediata al guardar, afecta solo transacciones nuevas

**Validación de Consistencia:**
- Al cambiar moneda, validar que todos los precios siguen siendo válidos
- Al cambiar impuesto, recalcular totales en carrito del POS (si hay uno activo)

**Notificación de Cambios:**
- Si hay usuarios con sesión activa cuando se cambia la configuración:
  - Notificar con mensaje: "La configuración del sistema ha sido actualizada"
  - Sugerir refrescar la página si es necesario
  - Actualizar automáticamente valores visibles (ideal)

**Preservación de Datos Históricos:**
- Las ventas anteriores mantienen:
  - El porcentaje de impuesto con el que fueron calculadas
  - La moneda original (aunque cambie la configuración)
- Esto evita discrepancias en reportes históricos

**Valores de Configuración en Base de Datos:**
- Almacenar como registro único por restaurante
- Incluir timestamps (created_at, updated_at)
- Registrar usuario que realizó el último cambio (audit)

**Configuración Inicial Obligatoria:**
- Al crear una cuenta nueva, solicitar configuración básica
- No permitir usar el sistema sin configurar al menos:
  - Nombre del restaurante
  - Moneda
  - Impuesto (puede ser 0%)
- La dirección es opcional

### Escenarios

---
