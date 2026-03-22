## HU-008: Cálculo y Actualización de KPIs

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción

### Criterios de Aceptación

**Cálculo de Ventas del Día:**
- Sumar el total de todas las órdenes con estado "Cerrada" del día actual (desde 00:00:00 hasta 23:59:59)
- El cálculo se realiza en el backend basado en la zona horaria del restaurante
- Incluir solo órdenes completadas (pagadas)
- Excluir órdenes canceladas o anuladas
- El valor se actualiza en tiempo real cuando se cierra una nueva orden

**Cálculo de Órdenes Abiertas:**
- Contar todas las órdenes con estados: "Pendiente", "Preparación" o "Lista"
- Excluir órdenes con estado "Cerrada"
- El conteo se actualiza en tiempo real cuando cambia el estado de una orden

**Cálculo de Ticket Promedio:**
- Fórmula: Total de ventas del día ÷ Número de órdenes cerradas del día
- Si no hay órdenes cerradas, el ticket promedio es $0.00
- Redondear a 2 decimales
- Se recalcula cada vez que se cierra una nueva orden
- El número de ventas consideradas debe coincidir exactamente con las órdenes cerradas del día

**Cálculo de Productos Más Vendidos:**
- Contar la cantidad vendida de cada producto en órdenes cerradas del día actual
- Ordenar por cantidad vendida de mayor a menor
- Tomar los primeros 5 productos
- Si un producto tiene múltiples ocurrencias en diferentes órdenes, sumar todas las cantidades
- Si hay productos con la misma cantidad vendida, ordenar alfabéticamente como criterio secundario
- Si no hay ventas del día, retornar array vacío

**Periodo de Cálculo (Día Actual):**
- "Día actual" se define desde las 00:00:00 hasta las 23:59:59 según la zona horaria del restaurante
- Al cambiar de día (después de medianoche), todos los KPIs se reinician automáticamente
- La zona horaria se configura en los datos del restaurante (configuración)

**Actualización en Tiempo Real:**
- Cuando se crea una orden nueva: actualizar "Órdenes abiertas"
- Cuando se cambia estado de orden: actualizar "Órdenes abiertas"
- Cuando se cierra una orden: actualizar "Ventas del día", "Ticket promedio", "Productos más vendidos", y "Órdenes abiertas"
- Las actualizaciones deben reflejarse en todos los dashboards abiertos (Owner y Cajero)

**Optimización de Performance:**
- Los KPIs se calculan en el backend, no en el frontend
- Usar caché con TTL de 30 segundos para evitar cálculos repetitivos
- Al crear/actualizar/cerrar orden, invalidar caché para forzar recálculo
- El frontend hace polling cada 30 segundos para obtener datos actualizados

**Validación de Datos:**
- Validar que las órdenes incluidas en cálculos pertenezcan al restaurante/sucursal correcta
- Validar que las fechas de las órdenes correspondan al día actual
- Validar que los totales de órdenes sean valores numéricos válidos (no negativos)

**Manejo de Casos Especiales:**
- Si el total de una orden es $0.00, no incluir en cálculo de ticket promedio
- Si un producto fue eliminado del menú pero tiene ventas del día, incluir en top 5 con su nombre original
- Si hay menos de 5 productos con ventas, retornar solo los que tienen ventas

### Escenarios

---
