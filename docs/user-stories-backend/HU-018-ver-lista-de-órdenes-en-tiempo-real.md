## HU-018: Ver Lista de Órdenes en Tiempo Real

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario (Owner o Cajero), quiero ver todas las órdenes del restaurante en tiempo real para monitorear el flujo de trabajo y gestionar los pedidos activos eficientemente.

### Criterios de Aceptación

**Filtros por Estado:**
- Tabs/pills horizontales:
  - "Todas" (por defecto, muestra todas las órdenes)
  - "Pendiente" (badge con número de órdenes pendientes)
  - "Preparación" (badge con número en preparación)
  - "Lista" (badge con número listas)
  - "Cerrada" (órdenes completadas)
- El filtro activo se destaca visualmente

**Tabla/Lista de Órdenes:**
- Columnas visibles:
  - Número de orden (ej: #001, #002)
  - Hora (hora de creación, formato 12h: "10:30 AM")
  - Items (número de productos, ej: "3 items")
  - Total (formato moneda)
- Cada fila es clickeable para abrir el detalle
- Las órdenes se ordenan por hora de creación (más reciente primero)

**Badges de Estado:**

**Actualización en Tiempo Real:**
- Las órdenes se actualizan automáticamente cada 10-15 segundos

**Botón de Actualización Manual:**

**Detalle Rápido en Fila:**
- Cada fila muestra información resumida
- Número de items: "3 items"
- Total: "$45.50"

**Estados de Carga:**
- La carga inicial debe completarse en menos de 2 segundos

**Manejo de Errores:**
- Si falla la actualización automática, seguir mostrando datos anteriores y permitir actualización manual

**Paginación:**
- Si hay más de 50 órdenes, implementar paginación

**Filtro por Fecha:**
- Dropdown para filtrar por fecha:
  - "Hoy" (por defecto)
  - "Ayer"
  - "Últimos 7 días"
  - "Este mes"
  - "Personalizado" (abre selector de rango de fechas)
- Al cambiar fecha, actualizar la lista de órdenes

**Búsqueda Rápida:**
- Búsqueda por número de orden (ej: "001", "#001")
- Búsqueda en tiempo real mientras se escribe (debounce de 300ms)

**Permisos:**
- Esta página es accesible tanto para Owner como para Cajero
- Ambos roles ven la misma información

### Escenarios

---
