## HU-033: Ver Lista de Ventas

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario Owner, quiero ver un listado completo de todas las ventas realizadas para tener control sobre los ingresos del restaurante y poder consultar transacciones específicas.

### Criterios de Aceptación

**Filtro por Fecha:**
- Dropdown con opciones predefinidas:
  - "Hoy" (por defecto)
  - "Ayer"
  - "Últimos 7 días"
  - "Este mes"
  - "Mes anterior"
  - "Personalizado" (abre date picker de rango)
- Al cambiar el filtro, actualizar la tabla automáticamente

**Date Picker Personalizado:**
- Al seleccionar "Personalizado", abrir selector de rango de fechas
- Permite seleccionar fecha inicial y fecha final
- Validar que fecha final >= fecha inicial
- Botones:
  - "Cancelar" (cierra sin aplicar)
  - "Aplicar" (ejecuta el filtro)

**Tabla de Ventas:**
- Columnas visibles:
  - Número de orden (ej: #001, #002)
  - Fecha (formato: "26 ene 2026")
  - Hora (formato 12h: "10:30 AM")
  - Método de pago (badge: Efectivo/Tarjeta)
  - Items (número de productos diferentes, ej: "3 items")
  - Total (formato moneda)
- Las ventas se ordenan por fecha y hora (más reciente primero)
- Cada fila es clickeable para abrir el detalle

**Badges de Método de Pago:**

**Formato de Totales:**
- Usar símbolo de moneda configurado en el sistema
- Formato con separador de miles y 2 decimales (ej: "$1,250.00")

**Resumen del Periodo:**
  - Total de ventas (número de transacciones)
  - Monto total vendido
  - Venta promedio
- Este resumen se actualiza según el filtro de fecha activo

**Ejemplo de Resumen:**
- "150 ventas | $3,250.00 total | $21.67 promedio"
- O en cards separadas:
  - "150 Ventas"
  - "$3,250.00 Total"
  - "$21.67 Promedio"

**Paginación:**
- Si hay más de 50 ventas, implementar paginación
- Botones: Anterior, 1, 2, 3, ..., Siguiente

**Búsqueda Rápida:**
- Búsqueda en tiempo real (debounce de 300ms)
- Busca por número de orden

**Estados de Carga:**
- La carga debe completarse en menos de 2 segundos

**Manejo de Errores:**

**Permisos:**
- Esta página solo es accesible para usuarios con rol Owner
- Si un Cajero intenta acceder, ver página 403 "No tienes permisos para acceder a esta sección"

### Escenarios

6. **Rango inválido**: Owner selecciona fecha final antes de fecha inicial, ve error "Rango de fechas inválido", no se ejecuta el filtro
11. **Resumen del periodo**: Owner filtra por "Este mes", ve en la parte superior "287 ventas | $6,500.00 total | $22.65 promedio"
17. **Cajero intenta acceder**: Usuario Cajero intenta navegar a `/sales`, ve página 403 "No tienes permisos para acceder a esta sección"

---
