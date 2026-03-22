## HU-036: Análisis Rápido del Periodo

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario Owner, quiero ver indicadores visuales y estadísticas rápidas del periodo seleccionado para tener una visión general del rendimiento de ventas sin necesidad de exportar datos.

### Criterios de Aceptación

**Ubicación de Estadísticas:**
- 3 cards principales en fila:
  - Total de ventas (cantidad)
  - Monto total vendido
  - Venta promedio

**Card: Total de Ventas**
- Número grande: cantidad de ventas del periodo
- Label: "Ventas" o "Total ventas"
- Ejemplo: "150 Ventas"

**Card: Monto Total Vendido**
- Monto en formato moneda, grande y destacado
- Label: "Total vendido" o "Ingresos"
- Ejemplo: "$3,250.00 Total"

**Card: Venta Promedio**
- Monto promedio en formato moneda
- Label: "Venta promedio" o "Ticket promedio"
- Cálculo: Total vendido ÷ Número de ventas
- Ejemplo: "$21.67 Promedio"

**Actualización Automática:**
- Las estadísticas se actualizan automáticamente al cambiar el filtro de fecha
- Al buscar una orden específica, las estadísticas NO cambian (siguen mostrando todo el periodo)

**Comparación con Periodo Anterior (Opcional):**
- Incluir pequeño indicador de cambio porcentual vs periodo anterior
- Flecha verde arriba si aumentó, flecha roja abajo si disminuyó
- Ejemplo: "↑ 15% vs periodo anterior"

**Desglose por Método de Pago:**
- Incluir card adicional o sección mostrando:
  - Ventas en efectivo (cantidad y monto)
  - Ventas con tarjeta (cantidad y monto)
- Formato visual: mini-gráfica de barras o números con porcentajes

**Ejemplo de Desglose:**
- "Efectivo: 85 ventas ($1,850.00) - 57%"
- "Tarjeta: 65 ventas ($1,400.00) - 43%"

**Periodo Sin Ventas:**
- Mensaje adicional: "No hay ventas registradas en este periodo"

**Estados de Carga:**
- Actualización debe completarse en menos de 2 segundos

**Manejo de Errores:**
- No bloquear el resto de la página, permitir ver la tabla de ventas

### Escenarios

2. **Estadísticas de periodo largo**: Owner filtra "Este mes" con 287 ventas y $6,500.00, ve estadísticas correctamente calculadas con promedio de $22.65
5. **Desglose por método de pago**: Owner ve desglose: "Efectivo: 85 ventas ($1,850.00) - 57%" y "Tarjeta: 65 ventas ($1,400.00) - 43%"

---

## Resumen de Funcionalidad de Historial de Ventas

**Información Incluida por Venta:**
- Número de orden (secuencial)
- Fecha y hora de la venta
- Método de pago (Efectivo/Tarjeta)
- Lista de productos vendidos
- Cantidades y precios
- Subtotal, impuesto y total
- Notas (si existen)
- Canal: Mostrador (fijo para MVP)

**Filtros Disponibles:**
- Hoy (por defecto)
- Ayer
- Últimos 7 días
- Este mes
- Mes anterior
- Personalizado (rango de fechas)

**Acciones Principales:**
- Ver lista de ventas
- Filtrar por fecha
- Buscar orden específica
- Ver detalle de venta
- Imprimir ticket
- Exportar CSV

**Estadísticas Calculadas:**
- Total de ventas (cantidad)
- Monto total vendido
- Venta promedio
- Desglose por método de pago

---

## Navegación en Historial de Ventas

**URLs:**
- `/sales` → Lista de ventas (historial)
- `/sales/[id]` → Detalle de venta específica

**Breadcrumbs:**
- `/sales`: Dashboard > Historial de Ventas
- `/sales/[id]`: Dashboard > Historial de Ventas > Orden #XXX

**Acceso:**
- Desde menú lateral: "Ventas" o "Historial"
- Desde dashboard (Owner): Card o enlace a ventas

---

## Notas Técnicas

**Permisos:**
- Solo Owner tiene acceso a historial de ventas
- Cajero NO puede acceder (recibe 403)
- Validar permisos en frontend y backend

**Performance:**
- Índices en: fecha, numero_orden, metodo_pago
- Paginación obligatoria para queries grandes
- Caché de estadísticas del día actual (TTL 5 minutos)
- Lazy loading en detalle de ventas

**Cálculos:**
- Venta promedio: Total vendido ÷ Número de ventas
- Redondear a 2 decimales
- Manejar división por cero (0 ventas = $0.00 promedio)

**Exportación CSV:**
- Generar en backend (no frontend)
- Limitar a 50,000 registros por exportación
- UTF-8 con BOM para compatibilidad con Excel
- Streaming para archivos grandes (evitar timeout)

**Datos Inmutables:**
- Las ventas son registros históricos inmutables
- No se pueden editar o eliminar (solo consultar)
- Preservar información incluso si productos/categorías se eliminan
- Soft delete no aplica (ventas siempre visibles para Owner)

**Timezone:**
- Usar zona horaria configurada en settings del restaurante
- Todas las fechas/horas en timezone local
- En CSV, incluir timezone o usar formato local

**Búsqueda:**
- Búsqueda por número de orden (exacto o parcial)
- Case-insensitive
- Soportar con o sin "#" (ej: "001" o "#001")

**Métodos de Pago:**
- Efectivo: Registrar monto recibido y cambio
- Tarjeta: Solo registro de autorización
- Preparar estructura para futuros métodos (Transferencia, etc.)

**Relación con Órdenes:**
- Una venta = Una orden en estado "Cerrada"
- Ventas provienen del POS (cierre directo)
- Órdenes de cocina que se cierran también son ventas
- Mismo ID de orden para venta y orden

**Formato de Impresión:**
- Optimizado para impresora térmica de tickets
- Ancho: 58mm o 80mm
