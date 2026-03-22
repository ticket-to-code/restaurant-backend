## HU-006: Dashboard para Usuario Owner

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario con rol Owner, quiero ver un dashboard completo con los KPIs principales de mi restaurante para tener una visión general del estado del negocio y tomar decisiones informadas.

### Criterios de Aceptación

**Card: Ventas del Día**
- Título: "Ventas del día"
- Valor principal: Monto total de ventas del día actual en formato moneda con 2 decimales (ej: "$1,250.00")
- Texto secundario: Fecha actual (ej: "26 de enero, 2026")

**Card: Órdenes Abiertas**
- Título: "Órdenes abiertas"
- Valor principal: Número total de órdenes con estados "Pendiente", "Preparación" o "Lista" (ej: "5")
- Texto secundario: Desglose por estado (ej: "3 en preparación, 2 listas")

**Card: Ticket Promedio**
- Título: "Ticket promedio"
- Valor principal: Promedio del valor de las órdenes completadas del día en formato moneda (ej: "$25.00")
- Texto secundario: Número de ventas consideradas (ej: "Basado en 50 ventas")
- Cálculo: Total de ventas del día ÷ Número de órdenes cerradas del día

**Card: Productos Más Vendidos (Top 5)**
- Título: "Productos más vendidos"
- Contenido: Lista de los 5 productos más vendidos del día
- Cada producto muestra:
  - Posición (#1, #2, #3, #4, #5)
  - Nombre del producto (truncado si es muy largo, máximo 30 caracteres)
  - Cantidad vendida (ej: "25 vendidos")
- Los productos se ordenan por cantidad vendida (descendente)

**Estados de Carga:**
- La carga debe completarse en menos de 2 segundos en condiciones normales

**Actualización de Datos:**
- Los KPIs se calculan en tiempo real basados en el día actual (desde 00:00 hasta 23:59)
- Al cambiar de día (pasada la medianoche), los KPIs se reinician automáticamente

**Manejo de Errores:**
- El error en un card no debe impedir que se muestren los demás

### Escenarios

---
